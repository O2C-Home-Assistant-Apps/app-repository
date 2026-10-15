# 0.4.0
## Features
- Monats-Heatmap mit stärkerem Kontrast – die Farbskala reicht vom sparsamsten bis zum verbrauchsstärksten Tag des Monats
- Einheitlicher, zum Farbschema passender Blauton für Tabs, Buttons, Schalter und Links in der ganzen App
- Kein Fokusrahmen mehr beim Anklicken von Buttons, Tabs und Kacheln (bei Tastaturbedienung weiterhin sichtbar)
- Farbpalette und Glow werden erst mit "Darstellung speichern" übernommen
- Analyse-Seite neu angeordnet - Verbrauchsübersicht oben, Grundlast und Spitzenleistung teilen sich die unterste Reihe
- Neue Schaltfläche "Zum Portal" unten auf "Mein Zuhause" öffnet das Living-Energy-Portal
- Hinweis "Daten werden gesammelt" steht jetzt unten auf allen drei Dashboards und lässt sich zu einem "i" einklappen und per Klick wieder öffnen
- Zugangsdaten für die Datenübertragung per QR-Code einlesen (Live-Kamera, Foto oder Link einfügen)
- Datenübertragung inkl. Einwilligung direkt im Einrichtungsassistenten einrichtbar
- Dashboards erscheinen schneller - die Karten bauen sich sofort auf und laden ihre Daten einzeln, statt hinter einem Vollbild-Ladekreis auf die erste Abfrage zu warten
- Kürzere Ladezeiten durch parallele Abfragen an Home Assistant (u. a. Verbrauchsstatistik, Live-Werte, Stundenverlauf, Monatsübersicht)
- Abschließen des Onboardings oder Ändern der Datenübertragung verwirft keine bereits geladenen Daten mehr
- Verbrauch und Analyse werden im Hintergrund vorgeladen, während "Mein Zuhause" angezeigt wird, und öffnen dadurch ohne Wartezeit
- Beim erneuten Öffnen der App wird sofort der zuletzt geladene Stand angezeigt (höchstens 24 Stunden alt) und im Hintergrund aktualisiert
- Weniger Last auf Home Assistant - automatische Aktualisierungen laufen zeitlich versetzt, pausieren, solange die App im Hintergrund ist, und mehrere Geräte bzw. Tabs teilen sich zwischengespeicherte Ergebnisse
## Fixed bugs
- Energiewalze zeigt wieder den untersten Wert der Leistungsskala
- Leistungswerte in Watt (Spitzenleistung, Grundlast, Diagramme) werden auf ganze Watt gerundet angezeigt
- Verbrauchskacheln "Heute", Monat und "Jahresschätzung" zeigen kWh mit einer Nachkommastelle
- Energiewalze zeigt nach mehrfachem Seitenwechsel nicht mehr "WebGL ist nicht verfügbar" und erholt sich nach einem Verlust des Grafikkontexts selbst
- Willkommensdialog und Einrichtungsassistent erscheinen nicht mehr erneut in jedem neuen Browser oder auf jedem neuen Gerät
- Weiterleitung nach dem Willkommensdialog führt wieder zum Dashboard
- Ohne eigenen Stromzähler konnten Verbrauchswerte durch die App-eigenen Hilfszähler stark überhöht sein (z. B. ein einzelner Tag mit tausenden kWh). Die Werte werden jetzt ausschließlich direkt aus dem Leistungssensor berechnet
- Ein Wechsel des Zeitraums im Verlaufsdiagramm geht nicht mehr verloren, wenn gleichzeitig eine Aktualisierung läuft
- Nach dem Zurücksetzen auf Werkseinstellungen zeigen die Dashboards keine alten Daten mehr an
- War Home Assistant beim Start der App nicht erreichbar, blieben Tagesgrenzen bis zum Neustart auf UTC - die Zeitzone wird jetzt erneut abgefragt
- Zeitraum-Kacheln (seit Monatsbeginn, Jahr, Kostenaufschlüsselung "Heute") rechnen beim ersten Laden in der Zeitzone von Home Assistant statt in der des Browsers
## Dependency updates
- Updated vue-router to 5.4.0
- Updated vue-i18n to 11.4.13
- Updated @vitejs/plugin-vue to 6.0.10
- Updated vite to 8.3.4
- Updated vite to 8.3.2
- Updated postcss to 8.5.29
- Updated gitlab.informatik.uni-bremen.de:5005/home-assistant/addon-uhb-mqtt-connector/app-uhb-mqtt-connector to 
- Updated gitlab.informatik.uni-bremen.de:5005/home-assistant/addon-uhb-mqtt-connector/app-uhb-mqtt-connector to 
- Updated node to 
- Updated vitest to 5.0.3
## Internal changes
- Hilfsentitäten "IM Grid Usage" / "IM Grid Export" (sensor.living_energy_grid_usage / _grid_export) samt Integrator, Backfill und Zustandsdatei entfernt; die App löscht beide Entitäten und die Datei beim Start
- Ungenutzte Endpunkte /api/ha/energy/range, /energy/today, /energy/totals und /energy/consumption entfernt
- Cache-Laufzeiten der regelmäßig abgefragten Endpunkte an die Abfrage-Intervalle des Frontends angepasst (5 Minuten bzw. 60 Sekunden)
- Server-Timing-Header an allen API-Antworten (Gesamtdauer, Zeit in HA-REST- und Statistik-Abfragen, Cache-Treffer) sowie Log-Zeile für langsame Anfragen (Schwelle über LE_SLOW_REQUEST_MS, Standard 1000 ms)
- Zählerstand seit Jahresbeginn überspringt die REST-Historie, sobald bekannt ist, dass der Recorder so weit nicht zurückreicht
***
# 0.3.0
## Features
- Neue Anordnung der Verbrauchsseite
- TOPAS Logo hinzugefügt
- Anzeige der Energiewalze überarbeitet
- Farbverlauf in der Enerergiewalze hinzugefügt
- Neue Anzeige 'Dein Tag im Vergleich'
- Neugestaltung der Energiewalzenansicht
## Fixed bugs
- WebUI für alle Nutzer (nicht nur Admins) freigeschaltet
- Einheiten und Rundung vereinheitlicht
- Bessere Darstellung von Kosten
- Verschiedene kleine Darstellungsbugs
- Einstellungen öffnen und Schließen vereinfacht
***
# 0.2.3
## Dependency updates
- Updated vue to 3.5.43
- Updated vue-i18n to 11.4.12
- Updated vite to 8.3.1
***
# 0.2.2
## Fixed bugs
- Anzeigefehler im Menü für mobile Geräte behoben
- Versprünge durch Berechnung halber Pixel bei manchen Bildschirmauflösungen behoben.
- Berechnung des Jahresverbrauchs resistenter gemacht
- Energiewalze aktuelle Zeit korrigiert
***
# 0.2.1
## Fixed bugs
- Fehlerhafte Anzeige der Verbrauchsübersicht behoben
- Akzentfarben angepasst
- Rundungen und Einheiten angepasst
- Energiewalze überarbeitet
***
# 0.2.0
## Features
- Darstellung der Energiewalze wurde angepasst
- Farbkontrast im Hellen Modus verbessert
- Optimierung von Hoveringauswahlen
- Verschiedene Optimierungen der Darstellung
## Fixed bugs
- Fehlerhafte Darstellung der Energiewalze im Hellen Modus behoben
- Berechnung der Verbrauch seit Kachel behoben
## Dependency updates
- Updated vue-router to 5.3.1
- Updated tailwindcss to 4.3.3
***
# 0.1.1
## Fixed bugs
- Behebt ein Cachingproblem, welches das Updaten der App erschwerte.
## Dependency updates
- Updated vue to 3.5.42
- Updated vue-i18n to 11.4.10
- Updated @vitejs/plugin-vue to 6.0.9
- Updated vite to 8.3.0
- Updated postcss to 8.5.28
- Updated node to 24.21.0
- Updated autoprefixer to 10.6.0
***
# 0.1.0
## Features
- Energiewalze added
## Internal changes
- Updated builsystem to workflow version 0.3.1
- Started creating a changelog
***
Versions up to `0.0.7` have no changelog.