import re

#iz cele spletne strani vzame link do izdelka
rx_link = re.compile(
    r'canonicalUrl":"(?P<link>.*?)","',
    flags=re.DOTALL
)

#iz izdelka razbere naslov, ceno, oceno in proizvajalca
rx_izdelek = re.compile(
    r'<h1.*?>(?P<title>.+?)</h1>.*?'
    r'<span itemprop="price".*?\$(?P<price>.*?)</span>.*?'
    r'<span class="f7 rating-number">\((?P<rating>.*?)\)</span>.*?'
    r'<a class="bg-transparent bn lh-solid pa0 sans-serif tc underline inline-button mid-gray pointer f6" href=".*?>(?P<brand>.*?)</a>',
    flags=re.DOTALL
)

#cena glede na kolicino
#v dolocenih primerih ne obstaja
rx_relativna_cena = re.compile(
    r'<span class="mr2">(?P<relative_price>.*?)</span>'
)

#iz izdelka razbere hranilno vrednost
#ce tukej dobim vrednost 'null,' pomeni da ni podatka, drugace pa zajamem podatke oblike '"stevilkaenota"'
#v dolocenih primerih ne obstaja
rx_hranilna_vrednost = re.compile(
    r'"Calories","amount":"(?P<calories>\d*?)".*?'
    r'"Total Fat","amount":(?P<fat>.*?),"dvp":(?P<fat_dvp>.*?),.*?'
    r'"Cholesterol","amount":(?P<cholesterol>.*?),"dvp":(?P<cholesterol_dvp>.*?),.*?'
    r'"Sodium","amount":(?P<sodium>.*?),"dvp":(?P<sodium_dvp>.*?),.*?'
    r'"Total Carbohydrate","amount":(?P<carbs>.*?),"dvp":(?P<carbs_dvp>.*?),.*?'
    r'"Protein","amount":(?P<protein>.*?),"dvp":(?P<protein_dvp>.*?),',
    flags=re.DOTALL
)