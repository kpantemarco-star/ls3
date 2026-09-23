import os
f=os.path.join(os.getcwd(),"yole")
if not os.path.exists(f):
    os.mkdir(f)
else:
    print("le fichier repertoire existe déja")
print(os.listdir(f))

equipe=os.path.join(os.getcwd(),"equipages.txt")
# -
# # print("Dossier courant :", os.getcwd())
# # print("Chemin recherché :", equipe)
# # print("Fichier trouvé ?", os.path.isfile(equipe))
# -
# with open(equipe, "r") as f:
#     contenu = f.read()
# print(contenu)



# exercice5
# nom_yole = input("entrer le nom de la yole ")
# while nom_yole != "" :
#     commune_yole = input("quelle est la commune de votre yole: ")
#     prenom_patron = input("quelle est le nom de votre patron: ")
#     nombre_equipage = input("quelle est le nombre de votre equipages: ")

#     with open(equipe,"a") as f:
#         f.writelines(nom_yole + ";" + commune_yole + ";" + prenom_patron + ";" + nombre_equipage + ";")

#     nom_yole = input("mettez un nom pour continuer laisser vide pour terminer ")

# with open(equipe, "r") as f:
#     contenue = f.read()
# print(contenue)


# with open(equipe, "r") as f:
#     n = 0 
#     lignes = f.readline()
#     while lignes != "":
#         n+=1
#         lignes = f.readline()
# print(n)


# exercice6
communiquer = os.path.join(os.getcwd(), "communique.txt")
with open(communiquer, "r") as c:
    contenue = c.read()
# print(repr(contenue))
print(contenue)
nom_yole = input("quelle est le nom de votre yole: ")
commune_yole = input("quelle est la commune de votre yole: ")
prenom_patron = input("quelle est le nom de votre patron: ")
contenue = contenue.replace("la yole gagnante", nom_yole)
contenue = contenue.replace("Le patron", prenom_patron)
contenue = contenue.replace("la commune", commune_yole)
print(contenue)
