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

    for i in range (len(vertices)) :
        vertices[i][0] = vertices[i][0] + translasi[i][0]
        vertices[i][1] = vertices[i][1] + translasi[i][1]
    return vertices

def rotate (vertices,r,a,b) :
    r = math.radians(r)
    rotasi = [[math.cos(r),-(math.sin(r)),0],[math.sin(r),math.cos(r),0],[0,0,1]]

    return kalimatriks(vertices,rotasi)
