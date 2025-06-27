==IIIF Loader V1==

  Dieses Python-Skript lädt hochauflösende Digitalisate aus METS- oder IIIF-Manifesten von ausgewählten Bibliotheken herunter. 
  Getestet an u. a. SLUB Dresden, BSB München, HAB Wolfenbüttel, SUB Göttingen und ULB Halle.
  Das Tool identifiziert die Bibliothek anhand einer URL, ruft das zugehörige METS- oder IIIF-Manifest ab 
  und lädt die verlinkten Bilddateien lokal herunter. 
  Es funktioniert wahlweise mit: direkten IIIF-/METS-Links oder Katalog-URLs (experimentell)
  
  Die Bilder werden in einem automatisch erzeugten Unterordner im Verzeichnis des Skripts gespeichert.

==Lizenz / Nutzung
  
  Dieses Tool ist frei nutzbar und kann gerne erweitert werden. Ein kurzer Hinweis bei Nutzung wäre nett.


==Verwendung
  1. Terminal am Speicherort des Skripts öffnen
  2. Starten mit:
    python "IIIF Loader V1.py"
  3.- Im Programm Menüpunkt wählen:
        (1) Direkten IIIF-/METS-Link eingeben
        (2) Katalog-URL eingeben (funktioniert nicht bei allen Anbietern)
        (3) Testrun mit vorbereiteten Beispielen

     Die Links zu IIF und METS finden sich zumeist direkt im Digitalisatviewer. 
     Beispiele für gültige Links:
      IIIF:
      https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb00053937/manifest
      METS:
      http://daten.digitale-sammlungen.de/~db/mets/bsb00020619_mets.xml



==Voraussetzungen

   Python 3.7 oder höher
   
   Python Dependencies:
   + bs4 (Beautiful Soup)
   + requests
  

==Fehlerbehandlung

  Bei Eingabe von py oder python im Terminal erscheint ggf. folgende Meldung: 'py' is not recognized as an internal or external command, operable program or batch file.
      -> Lösung: Python unter https://www.python.org herunterladen und bei der Installation „Add Python to PATH“ aktivieren.


Pull Requests und Issues willkommen.
Kontakt stefan.beckert@googlemail.com
