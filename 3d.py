import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from lalala import *

verticies = [
    [100, -100, -100,1],
    [100, 100, -100,1],
    [-100, 100, -100,1],
    [-100, -100, -100,1],
    [100, -100, 100,1],
    [100, 100, 100,1],
    [-100, -100, 100,1],
    [-100, 100, 100,1]
    ]

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

    glBegin(GL_LINES)
    glVertex3f(0.0, -500.0, 0.0)
    glVertex3f(0.0, 500.0, 0.0)
    glVertex3f(-500.0, 0.0, 0.0)
    glVertex3f(500.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0,-500.0)
    glVertex3f(0.0, 0.0,500.0)
    glEnd()

def DelOne(vertices) :
    a = []
    for i in vertices :
        b = []
        b.append(i[0])
        b.append(i[1])
        b.append(i[2])
        a.append(b)
    return a

def Cube(verticies):

    b = DelOne(verticies)

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(b[vertex])
    glEnd()

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


pygame.init()
display = (800,600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
gluPerspective(45, ((display[0])/display[1]), 0.1, 1000.0)
glTranslatef(0,0,-500)
while True:
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    Line()
    Cube(verticies)
    j = input()
    if j == 1 :
        print(verticies)
        verticies=translate3(verticies,10,10,10)
        print(verticies)
    elif j == 2 :
        print(verticies)
        verticies=rotate3(verticies,0,0,1)
        print(verticies)
    pygame.display.flip()
