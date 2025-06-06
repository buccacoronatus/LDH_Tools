==**VD16_txt2xml**==

Tool zur Konvertierung des txt Outputs des VD 16 Katalogs in strukturiertes und validies XML.

**Lizenz / Nutzung**

Dieses Tool ist frei nutzbar und kann gerne erweitert werden. Ein kurzer Hinweis bei Nutzung wäre nett.

**Verwendung** 
1. Über VD 16 Katalog speichern der gewünschten Suchergebnisse im Format Text (*.txt)
2. Die exportierte txt und das Pythonskript in denselben Ordner ablegen
3. Terminal im Ordner öffnen (z. B. Rechtsklick im Explorer → *„In Terminal öffnen“*)
4. Ausführen mit:
   py vd16_txt2xml.py {Name}.txt
  
  - Ersetze {Name}.txt durch den Namen deiner txt Datei (zumeist hitoutput(1).txt)
  - Ausgabe ist eine gleichnamige .xml-Datei mit dem Suffix _conv

**Voraussetzungen**
- Python 3.7 oder höher
- lxml Bibliothek (Installation über terminal: pip install lxml)

**Fehlerbehandlung** 
- Bei Eingabe von py oder python im Terminal erscheint ggf. folgende Meldung:
  'py' is not recognized as an internal or external command,
  operable program or batch file.

-> Lösung: Python unter https://www.python.org herunterladen und bei der Installation „Add Python to PATH“ aktivieren.

**Pull Requests und Issues willkommen – vor allem für**
    neue Exportformate (JSON, CSV, TEI-XML)
    bessere Fehlerbehandlung
    Mapping auf kontrollierte Vokabulare

**Kontakt** stefan.beckert@googlemail.com

    
