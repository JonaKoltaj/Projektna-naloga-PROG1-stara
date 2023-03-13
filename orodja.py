import csv
import json
import os


def pripravi_imenik(ime_datoteke):
    '''Če še ne obstaja, pripravi prazen imenik za dano datoteko.'''
    imenik = os.path.dirname(ime_datoteke)
    if imenik:
        os.makedirs(imenik, exist_ok=True)
    
def zapisi_csv(slovarji, imena_polj, ime_datoteke):
    '''Iz seznama slovarjev ustvari CSV datoteko z glavo.'''
    pripravi_imenik(ime_datoteke)
    with open(ime_datoteke, 'w', encoding='utf-8') as csv_datoteka:
        writer = csv.DictWriter(csv_datoteka, fieldnames=imena_polj)
        writer.writeheader()
        writer.writerows(slovarji)
        
        
      
def zapisi_json(objekt, ime_datoteke):
    pripravi_imenik(ime_datoteke)
    with open(ime_datoteke, 'w', encoding='utf-8') as json_datoteka:
        json.dump(objekt, json_datoteka, indent=4, ensure_ascii=False)
        
# def zapisi_json(objekt, ime_datoteke):
#     pripravi_imenik(ime_datoteke)
#     if os.path.getsize(ime_datoteke) == 0:
#         with open(ime_datoteke, 'w', encoding='utf-8') as json_datoteka:
#             json.dump(objekt, json_datoteka, indent=4, ensure_ascii=False)
#     else:
#         with open(ime_datoteke, 'r+', encoding='utf8') as jd:
#             json.load(jd)
#             jd.seek(-2)
#             json.dump