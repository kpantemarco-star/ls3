
# pour en savoir plus sur pylab , chercher pylab sur le web
import pylab

# F=pylab.gca ( ) # F peut-être vue comme un objet 'figure'

# def cercle( x , y , r) :
# # cercle de centre ( x , y ) et de rayon r
# # création du cercle :
# cir = pylab.Circle( [ x , y ] , radius=r , fill =False )
# # ajout du cercle à la figure :
# F.add_patch( cir )
# # ---------------------------------------------------
# def CerclesRec ( x , y , r ) :
# #construction récursive de la figure """
# cercle ( x , y , r)
# if r >1:
# CerclesRec ( x+3*r /2 , y , r /2 )
# CerclesRec ( x , y-3*r /2 , r /2 )

# # appel de l a fonction CerclesRec
# CerclesRec ( 0, 0,8)

# # pour placer toute l a fi gu r e dans un repère orthonormé :
# pylab.axis('scaled' )
# # affichage de la figure :
# pylab.show ( )

F= pylab.gca()
def cercle(x,y,r):
    cir = pylab.Circle([x,y], radius=r, fill = False)
F.add.patch(cir)
def cerclesRec (x,y,r):
    cercle(x,y,r)
    if r > 1: 
        CerclesRec(x+3*r /2 , y , r /2)
        CerclesRec ( x , y-3*r /2 , r /2 )
        
CerclesRec ( 0, 0,8)
pylab.axis('scaled' )
pylab.show ( )