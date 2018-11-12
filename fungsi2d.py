import math


def kalimatriks (vertices,transformasi) :
    brs = []

    for vertice in vertices :
        kol = []
        for j in range (len(transformasi)) :
            sum = 0
            for k in range (0,3) :
                sum = sum + (vertice[k]*transformasi[j][k])
            kol.append(sum)
        brs.append(kol)
    return brs

def translate (vertices,a,b) :
    translasi = [[1,0,a],[0,1,b],[0,0,1]]

    return kalimatriks(vertices,translasi)

def dilate (vertices,k) :
    dilatasi = [[k,0,0],[0,k,0],[0,0,1]]

    return kalimatriks(vertices,dilatasi)

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

def reflect (vertices,str) :
    if (str == "y") :
        refleksi = [[-1,0,0],[0,1,0],[0,0,1]]
    elif (str == "x") :
        refleksi = [[1,0,0],[0,-1,0],[0,0,1]]
    elif (str == "y=x") :
        refleksi = [[-1,0,0],[0,-1,0],[0,0,1]]
    elif (str == "(a,b)"):
        refleksi = [[1,0,0],[0,1,0],[0,0,1]]
    return kalimatriks(vertices,refleksi)

def custom (vertices,a,b,c,d):
    kustom = [[a,b,0],[c,d,0],[0,0,1]]
    return kalimatriks(vertices,kustom);

def  multiple(vertices,n):
    for i in range (0,n):
        inp = input()
        trans = inp.split(' ')
        if trans[0] == "translate":
            trf = translate(vertices,float(trans[1]),float(trans[2]))
        elif trans[0] == "dilate":
            trf = dilate(vertices,float(trans[1]))
        elif trans[0] == 'rotate':
            trf = rotate(vertices,float(trans[1]),float(trans[2]),float(trans[3]))
        elif trans[0] == 'reflect':
            trf = reflect(vertices,trans[1])
        elif trans[0] == 'shear':
            trf = shear(vertices,trans[1],float(trans[2]))
        elif trans[0] == 'stretch':
            trf = stretch(vertices,trans[1],float(trans[2]))
        elif trans[0] == 'custom':
            trf = custom(vertices,float(trans[1]),float(trans[2]),float(trans[3]),float(trans[4]))
        vertices = trf
    return vertices
