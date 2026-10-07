import csv
import os


date = input("la date de saisi: ")
ville = input("le nom de la ville: ")
temperatur = input(" la temperature: ")
h_vague = input("la hauteur des vague: ")

f = os.path.join(os.getcwd(), "releves1.csv")
if not os.path.exists(f):
    with open("releves1.csv", "w", newline="") as r: 
        w = csv.writer(r, delimiter=";")
        w.writerow(["date","ville","temperature","hauteur vague"])
        w.writerow([date, ville, temperatur, h_vague])
else:
    with open("releves1.csv", "a", newline="") as r: 
        w = csv.writer(r, delimiter=";")
        # w.writerow(["date","ville","temperature","hauteur vague"])
        w.writerow([date, ville, temperatur, h_vague])

station = input("station à consulter")
list_satation = []
with open("releves1.csv", "r", newline="") as r:
    w = csv.DictReader(r, delimiter=";")
    for ligne in w:
        if ligne["ville"] == station:
            list_satation.append(ligne)
print(list_satation)

station_cherchee = input("Nom de la station : ")

temperatures = []

with open("releves1.csv", newline="") as r:
    lecteur = csv.reader(r, delimiter=";")
    entete = next(lecteur)
    for ligne in lecteur:
        if ligne[1] == station_cherchee:
            temperatures.append(float(ligne[2]))

if temperatures:
    moyenne = sum(temperatures) / len(temperatures)
    print(f"Température moyenne à {station_cherchee} : {moyenne:.1f} °C ({len(temperatures)} relevé(s))")
else:
    print(f"Aucun relevé trouvé pour {station_cherchee}.")