import os 
# print(os.getcwd())
# os.mkdir("rep")
# os.chdir("rep")
# print(os.listdir("."))
# -----------------------
# os.remove("revleves")
# os.listdir("revleves")
# -------------------------
# chemin = os.path.join(os.getcwd(), "bidon.py")
# print(chemin)
# rep, fic = os.path.split(chemin)
# print("le dossier :", rep)
# print("le fichier :", fic)
# if not os.path.exists(chemin):
#     print("ce fichier n'existe pas (encore).")
# -----------------------------------------------------
# path = os.path.join(os.getcwd(),"journale.txt")
# if not os.path.exists(path):
#     print("le chemin n'existe pas ")
# else:
#     print("le chemin existe")

# f = open("journale.txt","a" )
# f.write("\nmardi")
# f.close
# --------------------------------------------------------
# |-------------------------|
# |correction du fragment 3 |
# | copier un text dans un  |
# | ligne par ligne         |
# |-------------------------|
# src = open("a.txt")
# dst = open("b.txt", "w")

# ligne = src.readline()
# while ligne != "":
#     dst.write(ligne)
#     ligne = src.readline()

# src.close()
# dst.close()

# --------------------------
# compter le nombre de ligne 
# dans un fichier text
# ---------------------------
# with open("a.txt") as f:
#     n = 0
#     for ligne in f:
#         n += 1

# print(n)