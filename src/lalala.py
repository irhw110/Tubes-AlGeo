import math

def kalimatriks (vertices,transformasi) :
    brs = []

    for vertice in vertices :
        kol = []
        for j in range (len(transformasi)) :
            sum = 0
            for k in range (0,4) :
                sum = sum + (vertice[k]*transformasi[j][k])
            kol.append(sum)
        brs.append(kol)
    return brs

def translate3 (vertices,a,b,c) :
    translasi = [[1,0,0,a],[0,1,0,b],[0,0,1,c],[0,0,0,1]]
    return kalimatriks(vertices,translasi)

def rotate3 (vertices,param,r,a,b,c):
    r = math.radians(r)
    rotasix = [[1,0,0,0],[0,math.cos(r),-(math.sin(r)),0],[0,math.sin(r),math.cos(r),0],[0,0,0,1]]
    rotasiy = [[math.cos(r),0,math.sin(r),0],[0,1,0,0],[-(math.sin(r)),0,math.cos(r),0],[0,0,0,1]]
    rotasiz = [[math.cos(r),math.sin(r),0,0],[-(math.sin(r)),math.cos(r),0,0],[0,0,1,0],[0,0,0,1]]
    vertices = translate3(vertices,-a,-b,-c)

    if param == "x" :
        return translate3(kalimatriks(vertices,rotasix),a,b,c)
    elif param == "y" :
        return translate3(kalimatriks(vertices,rotasiy),a,b,c)
    elif param == "z" :
        return translate3(kalimatriks(vertices,rotasiz),a,b,c)

    return kalimatriks(vertices,rotasi)

def dilate3 (vertices,k) :
    dilatasi = [[k,0,0,0],[0,k,0,0],[0,0,k,0],[0,0,0,1]]

    return kalimatriks(vertices,dilatasi)

def shear3 (vertices,param,k) :
    shearx = [[1,k,k,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    sheary = [[1,0,0,0],[k,1,k,0],[0,0,1,0],[0,0,0,1]]
    shearz = [[1,0,0,0],[0,1,0,0],[k,k,1,0],[0,0,0,1]]

    if param == "x" :
        return kalimatriks(vertices,shearx)
    elif param == "y" :
        return kalimatriks(vertices,sheary)
    elif param == "z" :
        return kalimatriks(vertices,shearz)

def stretch3 (vertices,param,k) :
    stretchx = [[k,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    stretchy = [[1,0,0,0],[0,k,0,0],[0,0,1,0],[0,0,0,1]]
    stretchz = [[1,0,0,0],[0,1,0,0],[0,0,k,0],[0,0,0,1]]

    if param == "x" :
        return kalimatriks(vertices,stretchx)
    elif param == "y" :
        return kalimatriks(vertices,stretchy)
    elif param == "z" :
        return kalimatriks(vertices,stretchz)

def reflect3 (vertices,str) :
    if (str == "xy") :
        refleksi = [[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,1]]
    elif (str == "xz") :
        refleksi = [[1,0,0,0],[0,-1,0,0],[0,0,1,0],[0,0,0,1]]
    elif (str == "yz") :
        refleksi = [[-1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    return kalimatriks(vertices,refleksi)

def custom3 (vertices,a,b,c,d,e,f,g,h,i):
    kustom = [[a,b,c,0],[d,e,f,0],[g,h,i,0],[0,0,0,1]]
    return kalimatriks(vertices,kustom);

def  multiple3(n):
    for i in range (0,n):
        l=inp
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
