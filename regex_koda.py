import re

# iz cele spletne strani vzame link do izdelka
rx_link = re.compile(
    r'canonicalUrl":"(.*?)["|\?]',
    flags=re.DOTALL
)

# iz niza razbere blok glavnih podatkov izdelka
rx_izdelek_blok_glavno = re.compile(r'<!DOCTYPE(.*?)<span class="b black">', flags=re.DOTALL)

rx_naslov = re.compile(r'<h1.*?>(.+?)</h1>', flags=re.DOTALL)
rx_proizvajalec = re.compile(r'<a class="bg-transparent bn lh-solid pa0 sans-serif tc underline inline-button mid-gray pointer f6" href=".*?>(.*?)</a>', flags=re.DOTALL)
rx_cena = re.compile(r'<span itemprop="price".*?\$(.*?)</span>', flags=re.DOTALL)
rx_ocena = re.compile(r'<span class="f7 rating-number">\((.*?)\)</span>', flags=re.DOTALL)
rx_relativna_cena = re.compile(r'<span class="mr2">(.*?)</span>', flags=re.DOTALL)

# iz niza razbere blok hranilnih vrednosti
rx_izdelek_hr_vred = re.compile(r'Calorie Information(.*?)<span class="b black">', flags=re.DOTALL)

# iz niza razbere cel izdelek
rx_izdelek = re.compile(r'<!DOCTYPE(.*?)<span class="b black">.*?Calorie Information(.*?)<span class="b black">', flags=re.DOTALL)

# za hranilne vrednosti je vedno enak niz, tako da jih zdruzimo
hranilne_vrednosti = ["Total Fat", "Cholesterol", "Sodium", "Total Carbohydrate", "Protein"]
niz = ''
for vrednost in hranilne_vrednosti:
    niz += '"' + vrednost + '"' + r',"amount":(.*?),"dvp":(.*?),.*?'

# iz izdelka razbere hranilno vrednost
# ce tukej dobim vrednost 'null,' pomeni da ni podatka, drugace pa zajamem podatke oblike '"stevilkaenota"'
# v dolocenih primerih ne obstaja
rx_hranilna_vrednost = re.compile(
    r'"Calories","amount":"(\d*?)".*?' + niz,
    flags=re.DOTALL
)
