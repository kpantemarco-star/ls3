import pylab
F = pylab.gca()
def rectangle(x,y,a,b):
    rec = pylab.Rectangle((x,y),a,b, fill =False)
    F.add_patch(rec)

def Rerectangle (x,y,a,b,sens='c'):
    rectangle(x,y,a,b)
    
    if a > 1 :
        if sens=='c':
            Rerectangle( x-(a/2), y, a/2, b/2,'g' )
            Rerectangle( (x+a/2), (y-(a/2)), a/2, b/2,'h' )
            Rerectangle(x, (y+a), a/2, b/2,'b')
            Rerectangle((x+a), (y+a/2), a/2, b/2,'d')
        elif sens == 'g':
            Rerectangle( x-(a/2), y, a/2, b/2,'g' )
            Rerectangle( (x+a/2), (y-(a/2)), a/2, b/2,'h' )
            Rerectangle(x, (y+a), a/2, b/2,'b')
        elif sens == 'd':
            Rerectangle( (x+a/2), (y-(a/2)), a/2, b/2,'h' )
            Rerectangle(x, (y+a), a/2, b/2,'b')
            Rerectangle((x+a), (y+a/2), a/2, b/2,'d')
        elif sens == 'h':
            Rerectangle( x-(a/2), y, a/2, b/2,'g' )
            Rerectangle( (x+a/2), (y-(a/2)), a/2, b/2,'h' )
            Rerectangle((x+a), (y+a/2), a/2, b/2,'d')
        elif sens == 'b':
            Rerectangle( x-(a/2), y, a/2, b/2,'g' )
            Rerectangle(x, (y+a), a/2, b/2,'b')
            Rerectangle((x+a), (y+a/2), a/2, b/2,'d')
            
Rerectangle(0,0,6,6)
pylab.axis('scaled')
pylab.show()
