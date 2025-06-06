import re, sys
from lxml import etree
from xml.sax.saxutils import escape

# Wandelt die txt Output file des VD 16 Katalogs in eine strukturierte 
# und valide XML für die Weiterverarbeitung um.   
# Initialize via terminal:
# py vd16_txt2xml.py txt datei
# Beispiel:
# py vd16_txt2xml.py txt hitoutput(1).txt 

# To do: 
# ++ JSON 
# +++ Database Export 

# SÄUBERT DIE KONVERTIERTEN DATEN FÜR VALIDES XML
def clean_for_xml(xml_input):
    if not isinstance(xml_input, str):xml_input=str(xml_input)
    xml_input=re.sub('[\x00-\x08\x0B\x0C\x0E-\x1F]', '', xml_input)
    xml_input=escape(xml_input)
    return xml_input


# ÖFFNEN DER DATEI ÜBER KOMMANDOZEILE
if len(sys.argv) < 2:
    print('please enter file name as argument:')
    print('example input: py konverter.py hitoutput(2).txt')
    input('press any key to exit')
    sys.exit(1)
file_name=sys.argv[1]
try: 
    with open(file_name, encoding='UTF-8') as f:
        file=f.read()
        print('--retrieved data from txt--')
except Exception as E: print('Error opening txt file: ', E)

# KONVERTIERUNG DER TXT IN PYTHON DICTIONARY
data_sets=file.split('\n\n')
data_list=list()
for data_set in data_sets:
    data={}
    data_set_l=data_set.strip().split('\n')
    if data_set_l != ['']:
        for x in data_set_l:
            data[x.split(': ',1)[0]]=x.split(': ',1)[1]
        data_list.append(data)


# XML KONVERTIERUNG
root=etree.Element('root')
for data in data_list:
    werk = etree.SubElement(root, 'Werk')
    for k,v in data.items():
        k=re.sub('^([0-9]+)','id\1',k)
        k=re.sub('/','_',k)
        k=clean_for_xml(k)
        v=clean_for_xml(v)
        try:node=etree.SubElement(werk, k)
        except Exception as E:print(f'Error converting {k} to xml:',f'RAW KEY: {repr(k)}\n', E)
        try:node.text=v
        except Exception as E:print(f'Error converting {v} to node text; RAW: {repr(v)}\n', E)
xml_tree=etree.ElementTree(root)

try:
    with open(f'{file_name.split('.txt')[0]}_conv.xml', 'wb') as file:
        xml_tree.write(file, encoding='UTF-8', xml_declaration=True, pretty_print=True)
    print(f'txt has been converted to {file_name.split('.txt')[0]}_conv.xml')
except:print('Error saving xml')

input('Press any key to quit')