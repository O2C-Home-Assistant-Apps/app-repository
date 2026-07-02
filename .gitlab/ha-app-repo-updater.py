import asyncio
import glob
import hashlib
import json
import logging
import os
import shutil
import sys

_logger = logging.getLogger("repo-updater")

TMP_REPO_FOLDER = "updater-repo-tmp"

async def run_git_command(args: list[str]):
    _logger.debug(f'Running git with args {" ".join(args)}')
    proc = await asyncio.create_subprocess_exec(
        'git', *args,
        stdout=asyncio.subprocess.DEVNULL,
        stderr=asyncio.subprocess.DEVNULL
    )

    await proc.wait()

    if proc.returncode != 0:
        _logger.error(f'Something went wrong trying to run git with args {" ".join(args)}')
        return False

    return True

async def clone_repo(repo_url: str):
    args = [
        "clone",
        repo_url,
        "--depth", "1",
        TMP_REPO_FOLDER
    ]

    return await run_git_command(args)

BUF_SIZE = 65536

def calculate_sha256(file: str):
    hasher = hashlib.sha256()

    with open(file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            hasher.update(data)

    return hasher.digest()

def update_files(app_dir: str, files: dict):
    changed = False

    for file, source_file in files.items():
        dst_file = os.path.join(app_dir, file)
        src_file = os.path.join(TMP_REPO_FOLDER, source_file)

        if os.path.isfile(dst_file) and calculate_sha256(src_file) == calculate_sha256(dst_file):
            continue

        os.rename(src_file, dst_file)
        changed = True

    return changed

async def commit_changes(app_dir: str):
    args = [
        "add",
        f"{app_dir}/*"
    ]

    if not await run_git_command(args):
        return False

    args = [
        "commit",
        "-m", f"Updated app {app_dir} from source repository [skip ci]"
    ]

    return await run_git_command(args)

async def process_app(app_dir, metadata: dict):
    if not await clone_repo(metadata["repository"]):
        return

    if update_files(app_dir, metadata["files"]):
        await commit_changes(app_dir)

    shutil.rmtree(TMP_REPO_FOLDER)

async def main():
    _logger.setLevel(logging.DEBUG)
    logging_handler = logging.StreamHandler(sys.stdout)
    logging_handler.setFormatter(logging.Formatter("[%(asctime)s] [%(name)s %(funcName)s] [%(levelname)s]: %(message)s"))
    _logger.addHandler(logging_handler)

    for path in glob.glob("*/updater-metadata.json"):
        app_dir = path.split("/")[0]
        with open(path, "r") as f:
            metadata = json.load(f)
        await process_app(app_dir, metadata)

if __name__ == "__main__":
    asyncio.run(main())
