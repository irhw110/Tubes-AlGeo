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

def rotate3 (vertices,a,b,c):
    rotasi = [[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,1]]
    return kalimatriks(vertices,rotasi)
