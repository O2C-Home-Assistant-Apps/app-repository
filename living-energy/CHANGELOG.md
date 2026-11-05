# 0.7.0
## Features
- „Dein Tag/Woche/Monat im Vergleich“ zeigt jetzt wie der eigene Zeitraum eine Prognoselinie bis zum Periodenende.
- Der Ampelverlauf in „Dein Tag/Woche/Monat im Vergleich“ geht jetzt fließend von Grün über Gelb und Orange zu Rot über und wird bei größerer Abweichung kräftiger.
- Auswahlen in der Ansicht „Verbrauch analysieren“ lassen sich mit Namen speichern (z. B. „Waschmaschine“). Gespeichert werden Zeitraum, Basis und die berechneten Werte zum Zeitpunkt des Speicherns – auch nachdem Home Assistant die fein aufgelösten Daten gelöscht hat.
- Gespeicherte Auswahlen erscheinen als Liste in der Ansicht „Verbrauch analysieren“; sie lassen sich dort bearbeiten, umbenennen und löschen und sind im Diagramm als Band markiert.
- Gespeicherte Auswahlen ab 10 Minuten aus den letzten 24 Stunden werden auf dem Live-Verbrauch (Energiewalze) markiert: Die Fläche zwischen gespeicherter Basis und Verbrauchskurve ist umrandet und schräg schraffiert. Steht eine Markierung vorne, erscheinen Name, Zeitraum, Verbrauch und Kosten in einer eigenen Zeile unter der aktuellen Leistung.
- Gespeicherte Auswahlen lassen sich nachträglich bearbeiten: „Bearbeiten“ lädt sie ins Diagramm, Zeitraum, Basis, Name und Farbe können angepasst und als Änderung oder als neue Auswahl gespeichert werden. Die Werte werden dabei neu berechnet.
- Jede Auswahl bekommt eine Farbe (Violett, Magenta, Türkis, Blau, Schwarz/Weiß). Sie wird vor dem Speichern gewählt – vorbelegt ist die erste noch unbenutzte – und lässt sich in der Liste über den Farbpunkt ändern.
- Verbrauch analysieren: Über den neuen Button „Analysieren“ unten links auf dem Live-Verbrauch (Energiewalze; auf dem Handy nur als Symbol) öffnet sich der Leistungsverlauf in feiner Auflösung – standardmäßig die letzten 24 Stunden, wahlweise 6 h oder 1 h, und bis zu etwa 10 Tage zurückblätterbar.
- In der Ansicht „Verbrauch analysieren“ lässt sich ein Zeitraum per Ziehen auswählen; angezeigt werden Netzbezug, Einspeisung und Kosten in diesem Zeitraum.
- Um den Verbrauch einzelner Geräte zu isolieren, kann eine Basis abgezogen werden: Mittel aus Leistung vor Start und nach Ende, nächtliche Grundlast, Minimum im Zeitraum oder ein eigener Wert. Der Mehrverbrauch über der Basis wird mit Kosten, Durchschnitts- und Spitzenleistung ausgewiesen.
- Die Kurve der Ansicht „Verbrauch analysieren“ verwendet dieselbe Farbskala wie die Energiewalze (Gelb bei 0 W über Orange bis Rot, Grün bis Blau bei Einspeisung).
- Zeiträume ohne Messwerte werden in der Ansicht „Verbrauch analysieren“ als Nulllinie gezeichnet statt als Lücke; in die Berechnung gehen sie weiterhin nicht ein.
- Die Ansicht „Verbrauch analysieren“ zeigt Verbrauch, Einspeisung und Kosten zusätzlich pro Stunde an.
- Die Ansicht „Verbrauch analysieren“ springt beim Blättern und Zoomen nicht mehr – auch dann nicht, wenn kein Lastspitzen-Vorschlag gefunden wird: Der Dialog ist oben verankert und die Ergebniskacheln bleiben stehen (mit „–“, solange nichts gewählt ist).
- Die 0-W-Linie ist im Diagramm der Ansicht „Verbrauch analysieren“ deutlich hervorgehoben.
- Die Basis lässt sich direkt im Diagramm über einen Schieberegler am rechten Rand verschieben.
- Die Auflösung der Ansicht „Verbrauch analysieren“ ist wählbar (Auto, Fein, 1 min, 5 min, 15 min); standardmäßig wird der Verlauf geglättet, damit er ruhiger und leichter lesbar ist.
- Beim Blättern und Zoomen gleitet die Ansicht weich zum neuen Zeitraum; die Blätter-Buttons zeigen an, um wie viel sie verschieben.
- Die Ansicht „Verbrauch analysieren“ schlägt automatisch einen Zeitraum um den größten Leistungsanstieg vor (Start vor dem Anstieg, Ende nach dem Abfall).
- Der Live-Verbrauch (Energiewalze) zeigt den Verlauf jetzt in 10-Minuten-Durchschnitten statt in Stundenmitteln. Geräte, die kürzer als eine Stunde laufen, sind damit deutlich als eigener Ausschlag zu sehen, und gespeicherte Auswahlen werden auf der Walze genauer markiert.
- Bei Einspeisung reicht die Skala der Energiewalze nach oben und unten nur noch so weit wie Bezug bzw. Einspeisung tatsächlich gehen, statt gespiegelt gleich weit. Die kleinere Seite behält mindestens ein Viertel der größeren, und die 0-Ebene ist kräftiger gezeichnet, damit sie erkennbar bleibt.
- Der Einwilligungstext zur Datenübertragung wurde auf das Forschungsprojekt Living-Energy aktualisiert (u. a. TOPAS als beteiligtes Institut, Zugang zu den eigenen Daten, Regeln zur Weitergabe).
- Nach der Zustimmung zur Datenübertragung lässt sich der Einwilligungstext unter Einstellungen → „Datenschutz & Datenübertragung“ über „Einwilligungstext ansehen“ jederzeit erneut lesen.
- Neue Einstellung „Ansicht“ (Einstellungen → System): „Einstieg“ zeigt das Wichtigste, „Erweitert“ alle Werkzeuge. Die Wahl gilt pro Browser, voreingestellt ist „Einstieg“.
- Infotexte im Einstiegsmodus wurden hinzugefügt.
- Live-Verbrauch (Energiewalze): Nach dem Drehen von Hand oder einem Antippen bleibt die Walze 5 Sekunden stehen und läuft dann sanft wieder an. Sie bleibt dort stehen, wo sie losgelassen wird; nur wer sie im Loslassen anschiebt, gibt ihr Schwung.
- Verbrauch analysieren: Die Farbauswahl ist eingeklappt und öffnet sich per Klick auf den Farbpunkt als kleines Menü; neben den fünf Farben lässt sich dort eine eigene Farbe wählen. Der Button heißt nur noch „Speichern“, damit auf dem Handy mehr Platz für den Namen bleibt.
- Die Liste der gespeicherten Auswahlen ist eingeklappt (mit Anzahl) und öffnet sich per Klick oder nach dem Speichern; „Umbenennen“ entfällt, der Name lässt sich über „Bearbeiten“ ändern. Auf dem Handy sind „Bearbeiten“ und „Löschen“ Symbole.
## Fixed bugs
- Unmögliche Messwerte des Leistungssensors (z. B. kurzzeitig 10³⁰ W) werden jetzt ignoriert und verfälschen Verbrauch, Statistiken und Live-Anzeige nicht mehr.
- Die Erklärung zum Monatskalender sprach vom „hellsten“ und „dunkelsten“ Feld – das stimmte nur im hellen Design. Jetzt heißt es „blassestes“ und „kräftigstes“ Feld.
- Auf dem Handy wurde die Zeile zur gespeicherten Auswahl unter dem Live-Verbrauch abgeschnitten; Name und Werte stehen dort jetzt in zwei Zeilen.
- Verbrauch analysieren: Lagen beide Auswahlgriffe übereinander (z. B. ganz links am Rand, auch nach einem Vorschlag), ließ sich die Auswahl nicht mehr verschieben. Jetzt entscheidet die Zugrichtung, welcher Griff bewegt wird, und die Griffe können sich beim Ziehen überholen.
## Dependency updates
- Updated vite to 8.3.5
- Updated postcss to 8.5.32
- Updated postcss to 8.5.31
- Updated node to v26.13.0
- Updated node to 26.13.0
## Internal changes
- Die Plausibilitätsprüfungen liegen jetzt eigenständig in core/checks.py (eine Funktion je Entitätsart); der Verlauf der Zähler für Bezug und Einspeisung läuft künftig ebenfalls durch eine Prüfung, die vorerst noch alle Werte durchlässt.
- Neue Endpunkte /api/marks (GET, POST, PATCH, DELETE); die Auswahlen liegen in /data/load_marks.json neben app_config.json. PATCH ändert einzelne Felder (Name, Farbe, Zeitraum, Basis, Werte); das Ergebnis wird als ganze Auswahl geprüft.
- Neuer Endpunkt /api/ha/power/samples liefert die vorzeichenbehaftete Leistung als zeitgewichtete Mittelwerte in festen Intervallen (10 s bis 5 min, max. 48 h je Abfrage); das Intervall ist per `step` wählbar und auf runde Uhrzeiten ausgerichtet.
- Neuer Endpunkt /api/ha/power/recent: die letzten 24 Stunden der Netzleistung als zeitgewichtete 10-Minuten-Mittel, an runden Uhrzeiten ausgerichtet. /api/ha/power/hourly bleibt für die Insights unverändert.
***
# 0.6.0
## Features
- Wer einspeist, bekommt einen Hinweis, wenn in den letzten 24 Stunden gleichzeitig eingespeist und Strom bezogen wurde, mit dem Betrag, der sich durch Verschieben des Verbrauchs hätte sparen lassen (ab 20 ct)
- Ist eine neue Version von Living-Energy verfügbar, erscheint ein Hinweis mit direktem Link zur Update-Seite in Home Assistant
- Die Kachel „Dein Tag/Woche/Monat im Vergleich“ hat eine vierte Auswahl für einen eigenen Zeitraum. Rückblick, Vorschau und Vergleichsbasis lassen sich frei einstellen; die Vorschau erscheint als Prognoselinie im Diagramm
- Abschlags-Check - in den Einstellungen lässt sich optional der Beginn des Abrechnungsjahres hinterlegen. Der Check betrachtet dann die zwölf Monate ab diesem Datum - bis heute gemessen, nur der Rest wird geschätzt. Ein bereits abgelaufener Zeitraum wird komplett aus Messwerten berechnet. Reichen die Zählerdaten nicht bis zum Startdatum zurück, wird wie bisher mit der Jahresschätzung gerechnet und das dazugesagt
## Fixed bugs
- Der Vorjahresvergleich der Jahresschätzung erscheint nur noch, wenn das Vorjahr vollständig erfasst ist, und vergleicht dieselben Tage beider Jahre
- Die Versionsanzeige in den Einstellungen zeigt nach einem Update nicht mehr die alte Version aus dem Browser-Cache an
- Tippfehler im Datenschutz-Kontakt der Einwilligungsseite korrigiert („Universität Bremen“)
## Dependency updates
- Updated vue to 3.5.44
- Updated vue-i18n to 11.4.16
- Updated vitest to 5.0.5
- Updated postcss to 8.5.30
- Updated node to 
- Updated node
## Internal changes
- Feedback, MQTT-Einrichtung und Datenschutz-Kontakt verweisen jetzt einheitlich auf support@living-energy.eu
***
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