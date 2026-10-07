import pylab
F = pylab.gca()

def triangle(xa, ya, xb, yb, xc, yc):
    tri = pylab.Polygon([(xa, ya), (xb, yb), (xc, yc)], fill=False)
    F.add_patch(tri)

def Retriangle(xa, ya, xb, yb, xc, yc):
    triangle(xa, ya, xb, yb, xc, yc)

    if yb - ya > 1:
        xab, yab = (xa + xb) / 2, (ya + yb) / 2
        xbc, ybc = (xb + xc) / 2, (yb + yc) / 2
        xca, yca = (xc + xa) / 2, (yc + ya) / 2

        Retriangle(xa,  ya,  xab, yab, xca, yca)   
        Retriangle(xab, yab, xb,  yb,  xbc, ybc)   
        Retriangle(xca, yca, xbc, ybc, xc,  yc)    

Retriangle(0, 0, 0, 8, 6, 4)
pylab.axis('scaled')
pylab.show()