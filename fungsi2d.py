import math


def kalimatriks (vertices,transformasi) :
    brs = []

    for vertice in vertices :
        kol = []
        for j in range (len(vertices)) :
            sum = 0
            for k in range (0,3) :
                sum = sum + (vertice[k]*transformasi[j][k])
            kol.append(sum)
        brs.append(kol)
    return brs

def translate (vertices,a,b) :
    translasi = [[1,0,a],[0,1,b],[0,0,1]]

    return kalimatriks(vertices,translasi)

def rotate (vertices,r,a,b) :
    r = math.radians(r)
    rotasi = [[math.cos(r),-(math.sin(r)),(a*(1-math.cos(r))+(b*math.sin(r)))],[math.sin(r),math.cos(r),(b*(1-math.cos(r))-(a*math.sin(r)))],[0,0,1]]

    return kalimatriks(vertices,rotasi)

def shear (vertices,param,k) :
    shearx = [[1,k,0],[0,1,0],[0,0,1]]
    sheary = [[1,0,0],[k,1,0],[0,0,1]]

    if param == "x" :
        return kalimatriks(vertices,shearx)
    elif param == "y" :
        return kalimatriks(vertices,sheary)

def stretch (vertices,param,k) :
    stretchx = [[k,0,0],[0,1,0],[0,0,1]]
    stretchy = [[1,0,0],[0,k,0],[0,0,1]]

    if param == "x" :
        return kalimatriks(vertices,stretchx)
    elif param == "y" :
        return kalimatriks(vertices,stretchy)
