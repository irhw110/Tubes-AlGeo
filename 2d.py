from OpenGL.GL import*
from OpenGL.GLUT import*
from OpenGL.GLU import*
from fungsi2d import *
import numpy as np
import serial
import os
import threading
import sys
import time

def Init_input(vertices) :
    N = int(input('Masukkan jumlah titik sudut : '))

    for i in range (N):
        #vertices.append([])
        inp = input('(x%d,y%d) '% (i+1,i+1))
        point = inp.split(',')
        a = []
        a.append(float(point[0]))
        a.append(float(point[1]))
        a.append(1.0)

        vertices.append(a)

    vertices = np.array(vertices)

    print(vertices)
    draw(vertices)
    return vertices

def draw(vertices) :

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(600)/float(600), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0,0.0,-1.4)
    glOrtho(-500, 500, -500, 500, 0.0, 1.0)

    glBegin(GL_LINES)
    glVertex3f(0.0, -500.0, 0.0)
    glVertex3f(0.0, 500.0, 0.0)
    glVertex3f(-500.0, 0.0, 0.0)
    glVertex3f(500.0, 0.0, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    for vertice in vertices:
        glVertex3fv(vertice)
    glEnd()
    glutSwapBuffers()

def func(vertices,default) :
    rot = False
    inp = input("Masukan fungsi : ")
    l=inp
    trans = inp.split(' ')
    if l == "0" :
        sys.exit()
    elif trans[0] == "translate":
        trf = translate(vertices,float(trans[1]),float(trans[2]))
    elif trans[0] == "dilate":
        trf = dilate(vertices,float(trans[1]))
    elif trans[0] == 'rotate':
        print(vertices)
        trf = rotate(vertices,float(trans[1]),float(trans[2]),float(trans[3]))
        print(trf)
    elif trans[0] == 'reflect':
        trf = reflect(vertices,trans[1])
    elif trans[0] == 'shear':
        trf = shear(vertices,trans[1],float(trans[2]))
    elif trans[0] == 'stretch':
        trf = stretch(vertices,trans[1],float(trans[2]))
    elif trans[0] == 'custom':
        trf = custom(vertices,float(trans[1]),float(trans[2]),float(trans[3]),float(trans[4]))
    elif trans[0] == 'multiple':
        trf = multiple(vertices,int(trans[1]))
    elif trans[0] == 'reset':
        trf = default
    vertices = trf
    draw(vertices)
    return vertices


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_ALPHA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(900,900)
glutInitWindowPosition(50,50)
vertices = []

glutCreateWindow("openGL Python 2D")
Init_input(vertices)
default = vertices
l = 1
while l != 0 :
    vertices=func(vertices,default)
