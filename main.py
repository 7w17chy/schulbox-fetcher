# Dieses script laedt eine zip-datei von schulbox.bildung.rlp.de herunter, unzipt sie, und vergleicht ihre groesse mit 
# der der zuvor heruntergeladenen datei. sollte sich die groesse veraendert haben, ist klar, dass es neue aufgaben gibt.
# natuerlich werden bei erneutem ausfuehren des scriptes alle "alten" dateien geloescht.
#
# coming soon:
#  - anzeigen welche dateien neu sind/wo sich etw. veraendert hat

import os, shutil, urllib.request
from zipfile import ZipFile

def loesche_ordner_oder_inhalte_wenn_voll(ordner):
    try:
        os.rmdir(ordner)
    except Exception as e:
        try:
            # wir hacken alles kurz und klein ...
            for hoffentlich_eine_datei in os.scandir(ordner):
                os.unlink(hoffentlich_eine_datei)
            # ... und versuchen es nochmal
            loesche_ordner_oder_inhalte_wenn_voll(ordner)
        except Exception as ee:
            print("Scheisse. War bestimmt Hr. Aumann der auf die Idee kam, geschachtelte Verzeichnisse zu erstellen? xD Versuch doch mal, es selbst zu fixen :D oder schreib mir wenn du keinen Bock hast.")

def aufraeumen():
    try:
        for datei in os.scandir('Download'):
            # wir wollen ordner ...
            if datei.is_dir():
                loesche_ordner_oder_inhalte_wenn_voll(datei)
            elif datei.is_file(): # ... und dateien ...
                # ... vernichten! freundlich fuer: "schmeiss den scheiss auf den misthaufen"
                os.unlink(datei)
            else:
                print("Ja, keine Ahnung was das ist...")
        # die zipdatei erstellt ein verzeichnis namens download, das kann auch weg...
        os.rmdir('Download')
        # die alte zipdatei kann auch weg
        os.unlink('zipdatei.zip')
    except Exception as e:
        print("Gut, keine Aufraeumarbeiten notwenig...")

# HIER GEHTS LOS
try:
    open('nicht_loeschen.txt')
    print('Cool, du hast die Datei also nicht geloescht :D')
except Exception as e:
    print('Die Datei \"nicht_loeschen.txt\" bitte wirklich nicht loeschen xD')
    open('nicht_loeschen.txt', 'w+').write(str('0'))

# erstmal aufraeumen, alle dateien die zuvor in dem verzeichnis waren loeschen (falls vorhanden)
aufraeumen()

# jetzt koennen wir die zip runterladen und speichern:
zip_datei = urllib.request.urlretrieve(open('LINK.txt').read().replace('\n', ''), 'zipdatei.zip')

# wir holen uns die groesse der alten zipdatei und der neuen:
gr_zipd_alt = int(open('nicht_loeschen.txt', 'r').read().replace('\n', ''))
gr_zipd_neu = os.stat('zipdatei.zip').st_size

# wir vergleichen die alte und die neue: wenn die neue groesser ist als die alte, dann koennen wir
# behaupten dass es neue aufgaben gibt, nur dann muessen wir sie auch entzippen, ansonsten loeschen
# wir sie wieder :)
if gr_zipd_alt < gr_zipd_neu:
    print('Es gibt neue Aufgaben! Packe sie dir in den Ordner \"Download\" aus...')
    zipdatei = ZipFile('zipdatei.zip')
    zipdatei.extractall()
    # die neue zipdatei ist jetzt die alte. wir muessen noch ihre groesse in die datei 'nicht_loeschen.txt' schreiben ('w' ueberschreibt)
    open('nicht_loeschen.txt', 'w').write(str(gr_zipd_neu))
    # die zipdatei kann jetzt weg
    os.unlink('zipdatei.zip')
else:
    print('Es gibt keine neuen Aufgaben! Loesche den ganzen alten Krempel mal...')
    aufraeumen()
