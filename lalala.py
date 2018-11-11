import math


def kalimatriks (vertices,transformasi) :
    brs = []

    for vertice in vertices :
        kol = []
        for j in range (len(vertices)) :
            sum = 0
            for k in range (0,4) :
                sum = sum + (vertice[k]*transformasi[j][k])
            kol.append(sum)
        brs.append(kol)
    return brs

def translate3 (vertices,a,b) :
    translasi = [[1,0,0,a],[0,1,0,b],[0,0,1,c],[0,0,0,1]]
    return kalimatriks(vertices,translasi)

def rotate3 (vertices,r,a,b,c):
    a = float(a);
    b = float(b);
    c = float(c);
    if(a==0) && (b==0) && (c==1):
		#rotasi terhadap sumbu z
		rotasi = [[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,1]]
	elif (a==0) && (b==1) && (c==0):
		#rotasi terhadap sumbu y
		rotasi = [[1,0,0,0],[0,-1,0,0],[0,0,1,0],[0,0,0,1]]
	elif (a==1) && (b==0) && (c==0):
		#rotasi terhadap sumbu x
		rotasi = [[-1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
	return kalimatriks(vertices,rotasi)
