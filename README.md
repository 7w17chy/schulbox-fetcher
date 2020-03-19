# There's a probably pretty bad English translation/explanation further down :) 
# schulbox-fetcher: Lass dich per Tastendruck über neue Aufgaben informieren :D
# Neue Aufgaben werden in neuem Browsertab geöffnet!
Du hast auch keinen Bock alle paar Stunden auf schulbox.bildung-rp.de zu gehen und in jedem Ornder nachzuschauen,
ob die Lehrer mal wieder was hochgeladen haben? Gut zu verstehen. Dieses Script macht genau das für dich:
Es lädt eine ZIP von Schulbox runter, entpackt sie, und vergleicht die Größen der frisch heruntergeladenen Ordner
mit denen der alten Ordner. Daran lässt sich feststellen, wo's neue Aufgaben gibt :)
Alles was du machen musst ist folgendes:

1. Gehe zu schulbox.bildung-rp.de 
2. Rechtsklick auf `Download all files`, Link kopieren
3. Den Link entweder in eine Datei namens `LINK.txt` oder direkt ins Script einfügen:

```python
# open(...).read().replace(..) durch den Link in einfachen Anführungszeichen ersetzen
zip_datei = urllib.request.urlretrieve(open('LINK.txt').read().replace('\n', ''), 'zipdatei.zip')
```
Fertig!

```sh
python3 main.py
```

Sollte den Rest für dich erledigen ^^ Wenn du prüfen möchtest, ob neue Aufgaben verfügbar sind, führe das Script einfach erneut aus :D
Wenn sich Python beschwert dass es einige Bibliotheken vermisst:

```sh
pip3 install zipfile urllib
```

# Warum nur schulbox.bildung-rp.de?
Weil dieses Script ein schnell Hingeschmiertes ist. Momentan ist alles sehr auf Schulbox fixiert (Pfade sind hardgecodet etc.),
aber das wird sich sicherlich bald ändern :) Wenn du Zeit und Lust hast, kannst du gerne eine Pull Request mit deinen Verbesserungen
einreichen :D

# Tool written in Python to notify the user about new exercises/news from their teachers.
Here in Rheinland-Pfalz, Germany, we've got a service called 'Schulbox'. It's basically a cloud (based on Nextcloud, I think), which allows
teachers to upload school materials like exercises as files, so that students can easily access it.
It is/was (depending on when you read it xD) heavily used during the corona crisis. Since it's really annoying to go to that website and search
through all folders to check whether new materials were uploaded or not, we/I wrote this script that downloads a zipfile from that service,
unpacks it and then compares the sizes of the folders with the sizes of the folders from a previous run and notifys you, whenever it detects
a larger folder size: there must be new material in that folder!
This tool currently only supports Schulbox, but it should also be capable of other services, if you want to help to add support for others too,
please send me a PM or make a pull request.
