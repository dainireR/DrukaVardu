import json

with open("uzd4.json", encoding="utf-8") as datne:
 dati=json.load(datne)
print(type(dati))
telefoni=[]
for vardnica in dati:
    modeli.append(vardnica["modelis"])
    modeli.sort()
    print(modeli)
#šis nav vajadzīgs
for vardnica in dati:
 print(vardnica["LMT"])
#šis nav vajadzīgs
for vardnica in dati:
    print(vardnica["Tet"])
#šis nav vajadzīgs
for vardnica in dati:
    print(vardnica["Euronics"])
# nepieciešams cikls, lai katru aprēķinātu atsevišķi
#netiek pievienots sarakstam
videja_cena=[]
vid=(vardnica["LMT"]+vardnica["Tet"]+vardnica["Euronics"])/3

#bibliotēkas importē visas augšā
import csv

datne.open("telefonu_analize.csv",encoding="utf-8")
satur=list(csv.reader(datne))#kāpēc jāpārveido par sarakstu? nepareiza metode ierakstam
print(satur)

datne.close()




