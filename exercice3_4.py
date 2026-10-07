import pylab
import random

# ---------- Fonctions de base (communes) ----------

def Rectangle(x, y, a, b):
    rect = pylab.Rectangle((x, y), a, b, fill=False)
    pylab.gca().add_patch(rect)

def cercle(x, y, r):
    """ cercle de centre (x, y) et de rayon r """
    cir = pylab.Circle([x, y], radius=r, fill=False)
    pylab.gca().add_patch(cir)

# ---------- Exercice 3 : Fractale 1 ----------

def Fractale1(cx, cy, c):

    Rectangle(cx - c/2, cy - c/2, c, c)
    cercle(cx, cy, c/4)

    if c > 1:
        Fractale1(cx - c/2, cy - c/2, c/2)   
        Fractale1(cx + c/2, cy - c/2, c/2)   
        Fractale1(cx - c/2, cy + c/2, c/2)   
        Fractale1(cx + c/2, cy + c/2, c/2)   

# ---------- Exercice 3 : Fractale 2 ----------

def Fractale2(x, y, a, b, sens=None):
    Rectangle(x, y, a, b)
    cercle(x + a/2, y + b/2, a/4)

    if a > 1 and b > 1:
        if sens != 's_o':
            Fractale2(x - a/2, y - b/2, a/2, b/2, 'n_e')
        if sens != 's_e':
            Fractale2(x + a,   y - b/2, a/2, b/2, 'n_o')
        if sens != 'n_o':
            Fractale2(x - a/2, y + b,   a/2, b/2, 's_e')
        if sens != 'n_e':
            Fractale2(x + a,   y + b,   a/2, b/2, 's_o')

# ---------- Exercice 4 : frontière fractale ----------

def frontiere(points, profondeur, perturbation):

    if profondeur == 0:
        return points

    nouveaux = []
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]

        # milieu du segment
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2

        
        dx, dy = x2 - x1, y2 - y1
        L = pylab.hypot(dx, dy)
        if L > 0:
            nx, ny = -dy / L, dx / L
        else:
            nx, ny = 0, 0

        r = random.uniform(-perturbation, perturbation)
        m = (mx + r * nx, my + r * ny)

        nouveaux.append((x1, y1))
        nouveaux.append(m)
    nouveaux.append(points[-1])

    return frontiere(nouveaux, profondeur - 1, perturbation / 2)

def trace(points, titre):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    pylab.plot(xs, ys, 'k-', linewidth=0.8)
    pylab.title(titre)
    pylab.axis('scaled')

# Frontière initiale : la Martinique, estimée sur la carte (x, y d'écran)
martinique_ecran = [
    (385,155), (430,170), (470,195), (510,225), (545,270), (575,260),
    (612,248), (590,282), (557,292), (570,325), (612,322), (565,350),
    (605,352), (610,385), (630,410), (655,435), (650,470), (672,510),
    (665,545), (640,575), (615,585), (600,565), (610,540), (590,520),
    (560,525), (520,518), (470,520), (445,530), (435,505), (425,480),
    (440,460), (465,445), (490,455), (515,445), (500,430), (490,400),
    (485,410), (470,410), (435,400), (400,375), (370,350), (350,310),
    (352,275), (330,245), (310,215), (315,180), (340,160), (385,155)
]
# l'axe y de l'écran est inversé : on prend -y
martinique = [(x, -y) for (x, y) in martinique_ecran]

# ---------- Programme principal ----------

Larg = 15   # essayer 3, 5, 15

# Figure 1
pylab.figure()
pylab.title("Fractale 1 (Larg=" + str(Larg) + ")")
Fractale1(Larg/2, Larg/2, Larg)
pylab.axis('scaled')

# Figure 2
pylab.figure()
pylab.title("Fractale 2 (Larg=" + str(Larg) + ")")
Fractale2(0, 0, Larg, Larg)
pylab.axis('scaled')

# Figure 3 : trait de côte de la Martinique
pylab.figure()
trace(frontiere(martinique, 4, 8), "Martinique")

pylab.show()