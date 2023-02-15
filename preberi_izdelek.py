import re
import regex_koda
import orodja
import preberi_strani_od_izdelkov

# vzame niz izdelka, vrne slovar glavnih podatkov
def izlusci_glavne_podatke(izdelek):
    podatki_izdelka = {}
    podatki = re.findall(regex_koda.rx_izdelek, izdelek)
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
    podatki_izdelka['Rating'] = float(podatki[0][2])
    podatki_izdelka['Price'] = float(podatki[0][3])
    return podatki_izdelka
    
# funkcija ki vzame niz in vrne touple oblike (cena, valuta, enota)
def str_to_touple_rel(vrednost):
    rx = r'\d+?\.\d+'
    cena = float(re.findall(rx, vrednost)[0])
    rx_1 = r'[¢|$]'
    valuta = re.findall(rx_1, vrednost)[0]
    rx_2 = r'/.+'
    enota = re.findall(rx_2, vrednost)[0].replace('/', '')
    return (cena, valuta, enota)
    
# vzame niz izdelka, vrne touple
def izlusci_relativno_ceno(izdelek):
    podatki = re.findall(regex_koda.rx_relativna_cena, izdelek)
    if len(podatki) != 0:
        rel_cena = str_to_touple_rel(podatki[0])
    else:
        rel_cena = ()
    return rel_cena

# ce je v imenu kolicina jo najdemo, ce je ni, je to posamicen izdelek
# vzame niz izdelka, vrne niz
def izlusci_kolicino(izdelek):
    podatki = re.findall(regex_koda.rx_izdelek, izdelek)
    ime = podatki[0][1]
    stevilka = re.findall(r'\d', ime)
    if len(stevilka) != 0:
        rx = r'\d+.*'
        niz = re.findall(rx, ime)[0]
    else:
        niz = 'Unit'
    return niz

# vzame slovar glavnih podatkov in mu doda relativno ceno(touple) ter kolicino(niz)
def glavni_podatki(izdelek):
    gl_pod = izlusci_glavne_podatke(izdelek)
    rel_cena = izlusci_relativno_ceno(izdelek)
    kolicina = izlusci_kolicino(izdelek)
    gl_pod['Relative Price'] = rel_cena
    gl_pod['Amount'] = kolicina
    return gl_pod

# funkcija, ki razbere kolicino in enoto iz vrednosti in vrne urejen par (kolicina, enota)
def str_to_touple(vrednost):
    kolicina = vrednost.replace('"', '')
    rx = r'[A-Za-z]'
    enota = ''.join(re.findall(rx, kolicina))
    niz = kolicina.replace(enota, '')
    if '.' in niz:
        return (round(float(niz)), enota)
    else:
        return (int(niz), enota)
    
# podobna funkcija kot zgoraj, le da vrne vedno (kolicina, '%')
def str_to_touple_dvp(vrednost):
    dvp = vrednost.replace('"', '')
    niz = dvp.replace('%', '')
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
            if podatki[0][2*i+2] == 'null':
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
            if podatki[0][0] == 'null':
                hr_vred[vrednost] = (0, 'g')
            else:
                hr_vred[vrednost] = str_to_touple(podatki[0][0])
            if podatki[0][1] == 'null':
                hr_vred[vrednost + ' DVP'] = (0, '%')
            else:
                hr_vred[vrednost + ' DVP'] = str_to_touple_dvp(podatki[0][1])
    return hr_vred
             
izdelki_glavno = []
for izdelek in range(len(preberi_strani_od_izdelkov.vsi_izdelki)):
    izdelki_glavno.append(glavni_podatki(izdelek))
    
hranilne_vrednosti = []
for izdelek in range(len(preberi_strani_od_izdelkov.vsi_izdelki)):
    hranilne_vrednosti.append(izlusci_vse_hranilne_vrednosti(izdelek))
    
izdelki = []
for i, izdelek in enumerate(range(len(preberi_strani_od_izdelkov.vsi_izdelki))):
    izdelki.append({izdelki_glavno[i]: hranilne_vrednosti[i]})
             
orodja.zapisi_json(izdelki, 'shranjene_datoteke/izdelki.json')
orodja.zapisi_csv(
    izdelki_glavno,
    ['Title', 'Price', 'Brand', 'Rating', 'Relative Price', 'Amount'], 'shranjene_datoteke/izdelki_glavno.json'
)
orodja.zapisi_csv(
    hranilne_vrednosti, ['Calories', "Total Fat", "Saturated Fat", "Trans Fat", "Polyunsaturated Fat", "Monounsaturated Fat", "Cholesterol", "Sodium", "Total Carbohydrate", "Dietary Fiber", "Sugars" "Protein"], 'obdelani-podatki/hranilne_vrednosti.csv'
    )
orodja.zapisi_csv(
    izdelki, ['film', 'oseba', 'vloga', 'mesto'], 'obdelani-podatki/izdelki.csv'
    )