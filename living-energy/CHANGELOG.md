# 0.5.0
## Features
- Wochenvergleich in der Monatsheatmap - Kalenderwochen lassen sich wie Tage als A und B auswählen und Tag für Tag nebeneinander vergleichen, mit Wochensumme und Abweichung in Prozent. Eine einzelne Woche wird wie bisher gegen den Schnitt der letzten Tage angezeigt
- Im Wochen-Tab des Verbrauchsvergleichs kann eine optionale zweite Woche gewählt werden
- "Dein Tag im Vergleich" hat jetzt eine Auswahl Tag / Woche / Monat. Die Woche wird stündlich gegen den Durchschnitt der letzten vier Wochen verglichen, der Monat täglich gegen denselben Monat im Vorjahr (ohne ausreichend Verlauf gegen den Schnitt der letzten drei Monate). Wie beim Tag gibt es Urteil, Kennzahlen, Hochrechnung und Verlaufskurve; die zuletzt gewählte Ansicht wird gemerkt
- Neuer Hinweis für Haushalte, die Strom einspeisen: An sonnigen Tagen nennt "Mein Zuhause" die voraussichtlich ertragreichsten drei Stunden des Tages (z. B. "zwischen 12:00 und 15:00 Uhr") als gute Zeit für Waschmaschine, Spülmaschine oder E-Auto - während des Zeitfensters als "jetzt, bis 15:00 Uhr". Grundlage sind die stündliche Wettervorhersage (Bewölkung) und der Sonnenstand am Standort des Hauses; ausgeblendet bleibt der Hinweis bis zum nächsten Tag. Benötigt eine Wetter-Entität
- Ist der Tag trüb und wird innerhalb der nächsten sechs Tage ein sonniger Tag vorhergesagt, schlägt ein Hinweis vor, aufschiebbare Verbraucher (Wäsche, Spülmaschine, E-Auto) dorthin zu verschieben ("morgen" bzw. "am Samstag"). Schweigt, wenn die stündliche Vorhersage heute doch ein sonniges Zeitfenster findet, und rund um die Wintersonnenwende, wenn die Sonne auch an klaren Tagen zu tief steht
- Speist der Haushalt gerade ein (im Schnitt der letzten 5 Minuten mindestens 500 W), sagt ein Hinweis, wie viel ins Netz geht, und dass jetzt ein guter Moment für Waschmaschine, Spülmaschine oder E-Auto ist. Er hat Vorrang vor der Wettervorhersage - der Hinweis, auf einen sonnigeren Tag zu warten, entfällt dann, ebenso das "jetzt" des Sonnen-Hinweises
- Die App heißt jetzt überall einheitlich "Living-Energy" (App-Store, Fenstertitel, Willkommensseite, Dokumentation)
- Neue Hinweise: Eine Glühbirne rechts neben der Begrüßung auf "Mein Zuhause" zeigt mit einer Zahl an, wenn neue Hinweise entdeckt wurden. Ein Klick öffnet die Hinweise darunter, über der Energiewalze. Gemeldet werden Veränderungen in beide Richtungen - Grundlast der letzten 2 Wochen gegenüber den 2 davor (mit Kosten pro Jahr), Verbrauch der letzten Woche gegenüber den 4 Wochen davor, tägliche Spitzen, der verbrauchsstärkste bzw. sparsamste Tag der letzten 30 Tage, der Monat gegenüber demselben Monat im Vorjahr, eine spürbare Nachzahlung bzw. ein Guthaben beim Abschlag sowie fehlender Strompreis oder Stromzähler
- Hinweise lassen sich ausblenden und unter "Ausgeblendete Hinweise" wieder ansehen und einblenden. Ein ausgeblendeter Hinweis erscheint von selbst wieder, wenn sich die Lage deutlich ändert (andere Richtung oder deutlich größere Abweichung). Gesehene und ausgeblendete Hinweise werden pro Browser gespeichert
- Die Glühbirne für die Hinweise leuchtet, solange die Hinweise geöffnet sind - das Glas wird gelb, der Glühfaden leuchtet auf, beim Öffnen läuft einmal ein Lichtring nach außen und danach glimmt ein sanfter Lichthof um die Birne (bei reduzierter Bewegung in den Systemeinstellungen ohne Animation)
- Heller Modus an die Standardfarben von Home Assistant angepasst
- Die Grundlast-Detailansicht zeigt jetzt, was die Grundlast kostet - pro Tag, Monat und Jahr in Euro und kWh, berechnet aus dem Mittelwert des gewählten Zeitraums und dem hinterlegten Arbeitspreis - sowie ihren Anteil am durchschnittlichen Tagesverbrauch
- Feedback direkt aus der App senden (Einstellungen → System) - es öffnet sich das eigene Mailprogramm mit einer vorbereiteten E-Mail an das Living-Energy-Team; App-Version und grobe technische Angaben werden mitgeschickt und vorher angezeigt, Entitätsnamen, Standort, Preise und Zugangsdaten nicht
- Haushalte, die Strom einspeisen, bekommen keine Hinweise mehr zu Wochenverbrauch, sparsamstem bzw. stärkstem Tag und Monat im Vorjahresvergleich - der Netzbezug folgt dort vor allem dem Wetter, nicht dem Haushalt
- "Dein Tag/Woche/Monat im Vergleich" weist bei Einspeisung darauf hin, dass der Netzbezug verglichen wird und sonnige bzw. trübe Tage den Wert verschieben
- Der Abschlags-Check gilt als grobe Schätzung, solange die Jahreskosten auf weniger als zwölf vollen Monaten beruhen, und sagt das dazu. Ein Hinweis auf Nachzahlung oder Guthaben erscheint erst danach
- Datenübertragung: Werden nach dem Einrichten Sensoren geändert, zeigt der Reiter "Datenschutz" in den Einstellungen eine 1. Dort steht, welche Sensoren übertragen werden und welche jetzt gewählt sind, und ein Knopf "Übertragung aktualisieren" übernimmt die aktuelle Auswahl. Bis dahin wird wie bisher unverändert das übertragen, was beim Einrichten gewählt war
- Abschlags-Check - in den Einstellungen lässt sich der monatliche Abschlag hinterlegen. Die Detailansicht der Jahresschätzung stellt dann zwölf Abschläge den geschätzten Jahreskosten gegenüber und zeigt die voraussichtliche Nachzahlung bzw. das Guthaben sowie einen passenden Abschlag
- Die Kachel "Jahresschätzung" zeigt bei hinterlegtem Abschlag die voraussichtliche Nachzahlung bzw. das Guthaben
## Fixed bugs
- Die Kachel "Jahresschätzung" zeigt bei hinterlegtem Abschlag jetzt tatsächlich die voraussichtliche Nachzahlung bzw. das Guthaben
## Dependency updates
- Updated vue-i18n to 11.4.14
## Internal changes
- Neuer Endpunkt /api/ha/energy/pace?period=week|month (Zählerstatistik, ohne Zähler aus den Mittelwerten des Leistungssensors); wird nur abgefragt, wenn Woche oder Monat ausgewählt ist
- /api/ha/forecast reicht zusätzlich cloud_coverage durch (null, wenn die Wetter-Integration es nicht liefert)
- /api/ha/energy/stats liefert zusätzlich energy.annual_months (Anzahl voller Monate hinter der Jahresschätzung)
- Neue Endpunkte GET /api/mqtt/status (übertragene vs. gewählte Sensoren) und POST /api/mqtt/update (Connector-Konfiguration neu schreiben und Connector neu starten)
***
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