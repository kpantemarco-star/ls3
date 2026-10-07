import os
f=os.path.join(os.getcwd(),"yole")
# if not os.path.exists(f):
#     os.mkdir(f)
# else:
#     print("le fichier repertoire existe déja")
# print(os.listdir(f))

# equipe=os.path.join(os.getcwd(),"equipages.txt")
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
# communiquer = os.path.join(os.getcwd(), "communique.txt")
# with open(communiquer, "r") as c:
#     contenue = c.read()
# # print(repr(contenue))
# print(contenue)
# nom_yole = input("quelle est le nom de votre yole: ")
# commune_yole = input("quelle est la commune de votre yole: ")
# prenom_patron = input("quelle est le nom de votre patron: ")
# contenue = contenue.replace("la yole gagnante", nom_yole)
# contenue = contenue.replace("Le patron", prenom_patron)
# contenue = contenue.replace("la commune", commune_yole)
# print(contenue)

# exercice7
# chronique = os.path.join(os.getcwd(), "chronique_etape1.txt")
# print(chronique)
# with open(chronique, "r") as e:
#     contenue = e.read()
# print(contenue)
# with open(chronique, "r") as c:
#     n=0
#     ligne = c.readline()
#     while ligne != "":
#         n+=1
#         ligne=c.readline()
# print(n)

# exercice8
# radio = os.path.join(os.getcwd(), "radio_etape2.txt")
# pointage = os.path.join(os.getcwd(), "pointages_etape2.txt")
# print(radio)
# print(pointage)
# with open(radio, "r") as r:
#     with open(pointage, "w") as p:
#         for ligne in r: 
#             ligne = ligne.replace("_"," ")

#             nouvelle_ligne = ""
#             espace = False

#             for c in ligne:
#                 if c == " ":
#                     if espace == False:
#                         nouvelle_ligne += ";"
#                         espace = True
#                 else:
#                     nouvelle_ligne += c
#                     espace = False

#             if nouvelle_ligne.endswith(";\n"):
#                 nouvelle_ligne = nouvelle_ligne[:-2] + "\n"

#             p.write(nouvelle_ligne)
            
# print(pointage)