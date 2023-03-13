import re
import regex_koda
import orodja

# vzame niz izdelka, vrne slovar glavnih podatkov
def izlusci_glavne_podatke(izdelek):
    podatki_izdelka = {}
    podatki = re.findall(regex_koda.rx_izdelek, izdelek)
    if len(podatki) != 0:
        brand = podatki[0][0]
        podatki_izdelka['Brand'] = brand
        # preverimo ce sta v imenu brand ali kolicina in ju odstranimo
        ime = podatki[0][1]
        stevilka = re.findall(r'\d', ime)
        if brand in ime:
            ime = ime.replace(brand + " ", "")
        if len(stevilka) != 0:
            rx = r',\s\d+.*'
            niz = ' '.join(re.findall(rx, ime))
            ime = ime.replace(niz, "")
        if 'Each' in ime:
            ime = ime.replace(", Each", "")
        podatki_izdelka['Title'] = ime
        podatki_izdelka['Price'] = float(podatki[0][2])
    else:
        podatki_izdelka['Brand'] = 'ni podatka'
        podatki_izdelka['Title'] = 'ni podatka'
        podatki_izdelka['Price'] = 0.0
    return podatki_izdelka

#vzame niz izdelka in vrne float
def izlusci_oceno(izdelek):
    podatki = re.findall(regex_koda.rx_ocena, izdelek)
    if len(podatki) != 0:
        ocena = float(podatki[0])
    else:
        ocena = 0.0
    return ocena
    
# funkcija ki vzame niz in vrne touple oblike (cena, valuta, enota)
def str_to_touple_rel(vrednost):
    rx = r'\d+?\.\d+'
    cena = float(re.findall(rx, vrednost)[0])
    rx_1 = r'[¢|$]'
    if len(re.findall(rx_1, vrednost)) != 0:
        valuta = re.findall(rx_1, vrednost)[0]
    else:
        valuta = '//'
    rx_2 = r'/.+'
    enota = re.findall(rx_2, vrednost)[0].replace('/', '')
    return (cena, valuta, enota)
    
# vzame niz izdelka, vrne touple
def izlusci_relativno_ceno(izdelek):
    podatki = re.findall(regex_koda.rx_relativna_cena, izdelek)
    if len(podatki) != 0:
        # vec podatkov dobimo, samo en izmed njih je prava cena, moramo ga izlusciti
        stevilke = r'\d+?\.\d+'
        st = re.findall(stevilke, ' '.join(podatki))
        if len(st) != 0:
            pravi_podatek = []
            for i in podatki:
                if st[0] in i:
                    pravi_podatek.append(i)
            if len(pravi_podatek)!= 0:
                rel_cena = str_to_touple_rel(pravi_podatek[0])
            else:
                rel_cena = ()
        else:
            rel_cena = ()
    else:
        rel_cena = ()
    return rel_cena

# ce je v imenu kolicina jo najdemo, ce je ni, je to posamicen izdelek
# vzame niz izdelka, vrne niz
# !!!TODO 2% milk etc
def izlusci_kolicino(izdelek):
    podatki = re.findall(regex_koda.rx_izdelek, izdelek)
    if len(podatki) != 0:
        ime = podatki[0][1]
        stevilka = re.findall(r'\d', ime)
        if len(stevilka) != 0:
            rx = r'\d+.*'
            niz = re.findall(rx, ime)[0]
        else:
            niz = 'Unit'
    else:
        niz = 'ni podatka'
    return niz

# vzame slovar glavnih podatkov in mu doda relativno ceno(touple) ter kolicino(niz)
def glavni_podatki(izdelek):
    gl_pod = izlusci_glavne_podatke(izdelek)
    rel_cena = izlusci_relativno_ceno(izdelek)
    kolicina = izlusci_kolicino(izdelek)
    ocena = izlusci_oceno(izdelek)
    gl_pod['Relative Price'] = rel_cena
    gl_pod['Amount'] = kolicina
    gl_pod['Rating'] = ocena
    return gl_pod

# funkcija, ki razbere kolicino in enoto iz vrednosti in vrne urejen par (kolicina, enota)
def str_to_touple(vrednost):
    kolicina = vrednost.replace('"', '')
    rx = r'[A-Za-z]'
    enota = ''.join(re.findall(rx, kolicina))
    niz = kolicina.replace(enota, '')
    failsafe = re.findall(rx, niz)
    if len(failsafe) != 0 or len(niz) == 0:
        return (0, '//')
    else:
        decimalka = re.findall(r'\d\.\d', niz)
        if len(decimalka) != 0:
            return (round(float(decimalka[0])), enota)
        else:
            return (int(niz), enota)
    
# podobna funkcija kot zgoraj, le da vrne vedno (kolicina, '%')
def str_to_touple_dvp(vrednost):
    dvp = vrednost.replace('"', '')
    niz = dvp.replace('%', '')
    rx = r'\d+'
    stevilka = re.findall(rx, niz)
    if len(stevilka) == 0:
        return (0, '%')
    else:
        return (int(niz), '%')

# vzame niz izdelka in vrne slovar hranilnih vrednosti, oblike "vrednost":(kolicina, enota)
def izlusci_hranilno_vrednost(izdelek):
    hr_vred = {}
    podatki = re.findall(regex_koda.rx_hranilna_vrednost, izdelek)
    if len(podatki) != 0:
        hr_vred['Calories'] = int(podatki[0][0])
        for i, vrednost in enumerate(regex_koda.hranilne_vrednosti):
            # locimo na prazne podatke in na neprazne
            if podatki[0][2*i+1] == 'null':
                hr_vred[vrednost] = (0, 'g')
            else:
                hr_vred[vrednost] = str_to_touple(podatki[0][2*i+1])
            if podatki[0][2*i+2] == 'null' or podatki[0][2*i+2] == '"test%"':
                hr_vred[vrednost + ' DVP'] = (0, '%')
            else:
                hr_vred[vrednost + ' DVP'] = str_to_touple_dvp(podatki[0][2*i+2])
    return hr_vred

# izluscimo se pomozne vrednosti, ki se vcasih pojavijo, vcasih ne
# vzame niz izdelka in vrne slovar vseh hr vrednosti, vlkjucno z glavnimi
def izlusci_vse_hranilne_vrednosti(izdelek):
    hr_vred = izlusci_hranilno_vrednost(izdelek)
    hranilne_vrednosti_sub = ["Saturated Fat", "Trans Fat", "Polyunsaturated Fat", "Monounsaturated Fat", "Dietary Fiber", "Sugars"]
    for vrednost in hranilne_vrednosti_sub:
        if '"' + vrednost + '"' in izdelek:
            rx_vrednost = re.compile('"' + vrednost + '"' + r',"amount":(.*?),"dvp":(.*?),', flags=re.DOTALL)
            podatki = re.findall(rx_vrednost, izdelek)
            # spet podobno kot pri prejsnji
            if len(podatki) != 0:
                if podatki[0][0] == 'null':
                    hr_vred[vrednost] = (0, 'g')
                else:
                    hr_vred[vrednost] = str_to_touple(podatki[0][0])
                if podatki[0][1] == 'null' or podatki[0][1] == '"test%"':
                    hr_vred[vrednost + ' DVP'] = (0, '%')
                else:
                    hr_vred[vrednost + ' DVP'] = str_to_touple_dvp(podatki[0][1])
    return hr_vred


# da jih ne usakic downloadam bom tukej samo odprla datoteke
vsi_izdelki = []
for i in range(25):
    with open('shranjene_datoteke/po_straneh/prvih_' + str(i) + '.txt', 'r', encoding='utf-8') as d:
        stran_izdelkov = d.read()
        vsi_izdelki.append(stran_izdelkov)

        
# shrani vse glavne podatke izdelkov v seznam slovarjev in nato zapisi v json in csv
from tqdm import tqdm
vsi_izdelki_glavno = []
for izdelki in vsi_izdelki:  
    izdelki_glavno = []
    for izdelek in tqdm(izdelki):
        izdelki_glavno.append(glavni_podatki(izdelek))
    vsi_izdelki_glavno.extend(izdelki_glavno)

# shrani vse ime izdelkov in vse hranilne vrednosti izdelkov v seznam slovarjev
vse_hranilne_vrednosti = []
for izdelki in vsi_izdelki:
    hranilne_vrednosti = []
    for izdelek in izdelki:
        podatek = {'Title': glavni_podatki(izdelek)['Title']}
        hr_vred = izlusci_vse_hranilne_vrednosti(izdelek)
        podatek.update(hr_vred)
        hranilne_vrednosti.append(podatek)
    vse_hranilne_vrednosti.extend(hranilne_vrednosti)

from tqdm import tqdm             
tqdm(orodja.zapisi_json(vse_hranilne_vrednosti, 'shranjene_datoteke/hranilne_vrednosti.json'))
tqdm(orodja.zapisi_json(vsi_izdelki_glavno, 'shranjene_datoteke/izdelki_glavno.json'))
tqdm(orodja.zapisi_csv(
    vsi_izdelki_glavno,
    ['Title', 'Price', 'Brand', 'Rating', 'Relative Price', 'Amount'],
    'shranjene_datoteke/izdelki_glavno.csv'
    ))
tqdm(orodja.zapisi_csv(
    vse_hranilne_vrednosti, ['Title', 'Calories', "Total Fat", 'Total Fat DVP', "Saturated Fat", "Saturated Fat DVP", "Trans Fat", "Trans Fat DVP", "Polyunsaturated Fat", "Polyunsaturated Fat DVP", "Monounsaturated Fat", "Monounsaturated Fat DVP", "Cholesterol", 'Cholesterol DVP', "Sodium", 'Sodium DVP', "Total Carbohydrate", "Total Carbohydrate DVP", "Dietary Fiber", "Dietary Fiber DVP", "Sugars", 'Sugars DVP', "Protein", 'Protein DVP'], 'shranjene_datoteke/hranilne_vrednosti.csv'
    ))