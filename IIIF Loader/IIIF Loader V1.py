# for debuggrun enter d after number
# for testrun enter 3

import urllib.request
import ssl, os
import json, requests, re
from bs4 import BeautifulSoup


ssl_context = ssl.create_default_context()

def detect_provider_and_signatur(url:str) -> tuple[str,str]| None:
    if 'opendata2.uni-halle.de' in url:
        return 'HALLE', url.split('//handle/')[1]
    elif 'katalog.slub-dresden.de' in url:
        return 'SLUB', url.split('id/0-')[1]
    elif 'www.digitale-sammlungen.de' in url:
        return 'BSB', url.split('/view/')[1].split('?page')[0]
    elif 'diglib.hab.de' in url:
        tei_url = url.split('/start.htm')[0] + '/tei-struct.xml'
        xml = urllib.request.urlopen(tei_url).read().decode()
        soup = BeautifulSoup(xml, 'xml')
        return 'HAB', soup.find('idno').text
    elif 'gdz.sub.uni-goettingen.de' in url:
        return 'SUB', url.split('/id/')[1]
    else:
        return None


def download(DOWNLOAD_LIST, switcher):
    print(f'Found {len(DOWNLOAD_LIST)} image urls')
    c=0
    while True:
        img_sel=input('\n---Download which images? (e.g. 1-14)\npress Enter to download all\n')
        if img_sel=='': break
        elif ('-') not in img_sel and re.fullmatch('\\d+', img_sel):
            c=int(img_sel)-1
            DOWNLOAD_LIST=DOWNLOAD_LIST[c:c+1]
            break
        try:
            img_sel_st=img_sel.split('-')[0]
            img_sel_en=img_sel.split('-')[1]
            DOWNLOAD_LIST=DOWNLOAD_LIST[int(img_sel_st)-1:int(img_sel_en)]
            c=int(img_sel_st)
            break
        except:continue
    
    for image_url in DOWNLOAD_LIST:
        print('downloading.')
        response=requests.get(image_url)
        if response.status_code==200:
            c=c+1
            sig_clean=re.sub(r'[<>:"/\\|?*]','-',signatur[0:20])
            folder_path=f'{sig_clean}'
            file_name=f'{sig_clean}_Image_{c:04d}.jpg'
            os.makedirs(folder_path, exist_ok=True)
            with open(os.path.join(folder_path,file_name),'wb') as file:
                file.write(response.content)
            print(f'---Download sucessfull: {image_url}')
            if 'd' in switcher:
                print('+++Debbuggingbreak+++')
                return
    print(f'\n\n+++images downloaded to:\n\n', os.path.abspath(folder_path), '\\\n\n')
    return

TESTLIST=(
r'https://katalog.slub-dresden.de/id/0-1651291160',
r'https://gdz.sub.uni-goettingen.de/id/PPN574841571',
r'https://opendata2.uni-halle.de//handle/1516514412012/1410',
r'https://diglib.hab.de/drucke/378-7-theol-2f/start.htm',
r'https://katalog.slub-dresden.de/id/0-1681391295',
r'https://www.digitale-sammlungen.de/de/view/bsb10164207?page=,1'
)

# HAUPTPROGRAMMROUTINE
while True: 
    URL_LIST=list()
    switcher=input('''
                   ------------Welcome to IIF and METS Loader------------------- 

                   (1) --   LINK TO IIIF OR METS 
                            for example: https://iiif.slub-dresden.de/iiif/2/175363900X/manifest.json
                            https://api.digitale-sammlungen.de/iiif/presentation/v2/bsb00053937/manifest

                   (2) --   SPECIFIC CATALOGUE URL (MIGHT FAIL!)
                            for example: https://katalog.slub-dresden.de/id/0-1651291160

                   ''').strip().lower()
    if switcher in ('1','2','3','1d','2d','3d'):
        break
    else: continue
if switcher in ('3','3d'):URL_LIST=TESTLIST
if switcher in ('1','2','1d','2d'):URL_LIST.append(input('please input url:\n').strip())

for ADDRESS in URL_LIST:
    DOWNLOAD_LIST=list()
    if switcher in ('2','3','2d','3d'): 
        result = detect_provider_and_signatur(ADDRESS)
        if not result:
            print(f"no available connection for {ADDRESS}")
            print('press any button to continue')
            continue
        archive, signatur = result

        XML_ADDRESSES= {
        'SLUB': f'https://digital.slub-dresden.de/oai?verb=GetRecord&metadataPrefix=mets&identifier=oai:de:slub-dresden:db:id-{signatur}',
        'HAB': f'http://oai.hab.de/?verb=GetRecord&metadataPrefix=mets&identifier=oai:diglib.hab.de:ppn_{signatur}',
        'BSB': f'https://daten.digitale-sammlungen.de/~db/mets/{signatur}_mets.xml',
        'SUB': f'https://gdz.sub.uni-goettingen.de/mets/{signatur}.mets.xml',
        'HALLE': f'https://opendata2.uni-halle.de/oai/dd?verb=GetRecord&metadataPrefix=mets&identifier=oai:opendata2.uni-halle.de:{signatur}'
        }

        IIIF_ADDRESSES={
        'SLUB': f'https://iiif.slub-dresden.de/iiif/2/{signatur}/manifest.json',
        'HAB': f'NOT AVAILABLE',
        'BSB': f'https://api.digitale-sammlungen.de/iiif/presentation/v2/{signatur}/manifest',
        'SUB': f'https://manifests.sub.uni-goettingen.de/iiif/presentation/{signatur}/manifest',
        'HALLE': f'https://opendata2.uni-halle.de//json/iiif/{signatur}4adcc05f-5366-4709-82e6-e609d5e0a731/manifest'
            }
    
    try: # METS DOWNLOAD
        try:
            if switcher in ('2','3','2d','3d'): html = urllib.request.urlopen(XML_ADDRESSES[archive]).read().decode()
            if switcher in ('1','1d'): html = urllib.request.urlopen(ADDRESS).read().decode()
        except Exception as E:
            print(f'error: {E}')
            continue
        soup=BeautifulSoup(html,'xml')
        signatur=soup.find('title').text
        print('\nTitel: ', signatur, '\n\n')
        fileGrps=soup.find_all('fileGrp')
        for fileGrp in fileGrps:
            if fileGrp.get('USE') in ('ORIGINAL', 'MAX'):
                for Flocat in fileGrp.find_all('FLocat'):
                    DOWNLOAD_LIST.append(Flocat.get('xlink:href'))
        try:download(DOWNLOAD_LIST, switcher)
        except Exception as E: print(f'Error downloading: {E}')

    except: # +++ IIF Download  
        print('+++IIIF Download+++') 
        try: 
            if switcher in ('2','3','2d','3d'):html = urllib.request.urlopen(IIIF_ADDRESSES[archive]).read().decode()
            if switcher in ('1','1d'):
                html = urllib.request.urlopen(ADDRESS).read().decode()
        except Exception as E:
            print(f'error: {E}')
            continue
        
        j_html=json.loads(html)
        signatur=j_html['label']
        print('\nTitel: ', signatur, '\n\n')
        canvases=j_html['sequences'][0]['canvases']
        for canvase in canvases:
            DOWNLOAD_LIST.append(canvase['images'][0]['resource']['@id'])
        try:download(DOWNLOAD_LIST, switcher)
        except Exception as E: print(f'Error downloading from: {E}')

