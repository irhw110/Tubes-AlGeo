import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#Titik sudut dari kubus
edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )


def Line() :
#Fungsi menggambar sumbu koordinat 3d
    glBegin(GL_LINES)
    glVertex3f(0.0, -50000.0, 0.0)
    glVertex3f(0.0, 50000.0, 0.0)
    glVertex3f(-50000.0, 0.0, 0.0)
    glVertex3f(50000.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0,-50000.0)
    glVertex3f(0.0, 0.0,50000.0)
    glEnd()

def Cube(verticies):
#Fungsi untuk menggambar kubus
    b = DelOne(verticies)

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(b[vertex])
    glEnd()

def DelOne(vertices) :
#Fungsi untuk mengubah kubus yg awalnya matriks 8x4 menjadi 8x3 agar bisa digambar
    a = []
    for i in vertices :
        b = []
        b.append(i[0])
        b.append(i[1])
        b.append(i[2])
        a.append(b)
    return a