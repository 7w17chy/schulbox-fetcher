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
            print("Och ne, error: " + str(ee))

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
    except Exception as e:
        print("Gut, keine Aufraeumarbeiten notwenig...")

def lade_alt():
    f = open('nicht_loeschen.txt', 'r').split(';')
    alt = {}
    i = alt.len()
    j = 0
    while j < i:
        alt[f[j]] = int(f[j+1])
        j += 1
    return alt

def lade_neu():
    neu = {}
    for datei in os.scandir('Download'):
        neu[str(datei)] = os.stat(datei).st_size

def update_datei(dictio):
    f = open('nicht_loeschen.txt', 'w')
    for fach, groesse in dictio.items():
        f.write(str(fach) + ";" + str(groesse))

def check_neu():
    alt = lade_alt()
    neu = lade_neu()
    neue_aufgaben = False

    for fach, groesse in neu.items():
        if not fach in alt:
            print("Neues fach entdeckt: " + fach)
        else:
            if alt.get(fach) < neu.get(fach):
                print("Neue Aufgaben in Fach " + fach)
                neue_aufgaben = True

    if neue_aufgaben:
        update_datei(neu)


try:
    open('nicht_loeschen.txt')
    print('Cool, du hast die Datei also nicht geloescht :D')
except Exception as e:
    print('Die Datei \"nicht_loeschen.txt\" bitte wirklich nicht loeschen xD')
    open('nicht_loeschen.txt', 'w+').write(str('0'))

# ein bisschen sauber machen
aufraeumen()

# jetzt koennen wir die zip runterladen und speichern:
zip_datei = urllib.request.urlretrieve(open('LINK.txt').read().replace('\n', ''), 'zipdatei.zip')

# auspacken
zipdatei = ZipFile('zipdatei.zip')
zipdatei.extractall()

# checken
check_neu()

# und ein bisschen aufraeumen
os.unlink('zipdatei.zip')
