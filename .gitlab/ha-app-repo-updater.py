import asyncio
import glob
import hashlib
import json
import logging
import os
import shutil
import sys
from copy import deepcopy

from semver import Version

_logger = logging.getLogger("repo-updater")

TMP_REPO_FOLDER = "updater-repo-tmp"

async def run_git_command(args: list[str], return_stdout: bool = False):
    _logger.debug(f'Running git with args {" ".join(args)}')
    proc = await asyncio.create_subprocess_exec(
        'git', *args,
        stdout=asyncio.subprocess.PIPE if return_stdout else asyncio.subprocess.DEVNULL,
        stderr=asyncio.subprocess.DEVNULL
    )

    await proc.wait()

    stdout = ""
    if proc.stdout:
        stdout = (await proc.stdout.read()).decode(encoding="utf-8")

    if proc.returncode != 0:
        _logger.error(f'Something went wrong trying to run git with args {" ".join(args)}')
        if return_stdout:
            return False, stdout
        else:
            return False

    if return_stdout:
        return True, stdout
    else:
        return True

async def clone_repo(repo_url: str, branch=None):
    args = ["clone"]

    if branch:
        args.extend(["-b", branch])

    args.extend([
        "--depth", "1",
        "--",
        repo_url,
        TMP_REPO_FOLDER,
    ])

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
        "-m", f"Updated app {app_dir} from source repository"
    ]

    return await run_git_command(args)

async def get_remote_tags(repo_url: str) -> list[str] | None:
    args = [
        "ls-remote", "--tags", repo_url
    ]

    success, stdout = await run_git_command(args, return_stdout=True)

    if not success:
        return None

    tags = list()

    for line in stdout.splitlines():
        tag = line[line.rindex("/")+1:]
        tags.append(tag)

    return tags

async def process_git_tag_update(app_dir: str, metadata: dict):
    tags = await get_remote_tags(metadata["repository"])

    if not tags:
        return

    versions = list()
    for tag in tags:
        try:
            prefix = ""
            if tag.startswith("v"):
                prefix = "v"
                tag = tag[1:]
            versions.append((Version.parse(tag), prefix))
        except ValueError:
            continue

    remote_version, prefix = sorted(versions, key=lambda x: x[0])[-1]

    local_version = Version.parse("0.0.0")

    try:
        local_version = Version.parse(metadata["synced_version"])
    except (ValueError, KeyError):
        pass

    if remote_version == local_version:
        return

    if not await clone_repo(metadata["repository"], prefix + str(remote_version)):
        pass

    if update_files(app_dir, metadata["files"]):
        new_metadata = deepcopy(metadata)
        new_metadata["synced_version"] = str(remote_version)
        with open(app_dir + "/updater-metadata.json", "w") as f:
            f.write(json.dumps(new_metadata, indent=4))
        await commit_changes(app_dir)

async def process_app(app_dir, metadata: dict):
    if "strategy" in metadata and metadata['strategy'] == "git-tag":
        await process_git_tag_update(app_dir, metadata)
    else:
        if not await clone_repo(metadata["repository"]):
            return

        if update_files(app_dir, metadata["files"]):
            await commit_changes(app_dir)

    shutil.rmtree(TMP_REPO_FOLDER, ignore_errors=True)

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
