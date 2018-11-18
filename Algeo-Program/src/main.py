import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from render import *
from matrixOperation import *



#Sisi dari kubus, digunakan untuk reset ke semula
default3d = [
    [1, -1, -1,1],
    [1, 1, -1,1],
    [-1, 1, -1,1],
    [-1, -1, -1,1],
    [1, -1, 1,1],
    [1, 1, 1,1],
    [-1, -1, 1,1],
    [-1, 1, 1,1]
    ]

def func3(vertices) :
    inp = input("Masukan fungsi : ")
    l=inp
    trans = inp.split(' ')
    if l == "0" :
        sys.exit()
    elif trans[0] == "translate":
        trf = translate3(vertices,float(trans[1]),float(trans[2]),float(trans[3]))
    elif trans[0] == "dilate":
        trf = dilate3(vertices,float(trans[1]))
    elif trans[0] == 'rotate':
        print(vertices)
        trf = rotate3(vertices,(trans[1]),float(trans[2]),float(trans[3]),float(trans[4]),float(trans[5]))
        print(trf)
    elif trans[0] == 'reflect':
        trf = reflect3(vertices,trans[1])
    elif trans[0] == 'shear':
        trf = shear3(vertices,trans[1],float(trans[2]))
    elif trans[0] == 'stretch':
        trf = stretch3(vertices,trans[1],float(trans[2]))
    elif trans[0] == 'custom':
        trf = custom3(vertices,float(trans[1]),float(trans[2]),float(trans[3]),float(trans[4]))
    elif trans[0] == 'multiple':
        trf = multiple3(vertices,int(trans[1]))
    elif trans[0] == 'reset':
        trf = default3d
    vertices = trf
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #Clear screen
    Line()
    Cube(vertices)
    return vertices


def func2d(vertices,default) :
#Menu pilihan fungsi
    inp = input("Masukan fungsi 2D: ")
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
    Draw(vertices)
    return vertices

def threeDimen():
    verticies = [
    [1, -1, -1,1],
    [1, 1, -1,1],
    [-1, 1, -1,1],
    [-1, -1, -1,1],
    [1, -1, 1,1],
    [1, 1, 1,1],
    [-1, -1, 1,1],
    [-1, 1, 1,1]
    ]

    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, ((display[0])/display[1]), 0.1, 1000.0) # Mengatur perspektif gambar
    glTranslatef(0,0,-10)
    Line()
    Cube(verticies)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glRotatef(1, 0, 1, 0)
                if event.key == pygame.K_RIGHT:
                    glRotatef(-1, 0, 1, 0)

                if event.key == pygame.K_UP:
                    glRotatef(1, 1, 0, 0)
                if event.key == pygame.K_DOWN:
                    glRotatef(-1, 1, 0, 0)

                if event.key == pygame.K_f:
                    verticies=func3(verticies)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Line()
        Cube(verticies)
        pygame.display.flip()
        pygame.time.wait(10)

def twoDimen():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, ((display[0])/display[1]), 0.1, 1000.0) # Mengatur perspektif gambar
    glTranslatef(0,0,-10)
    Line()
    pygame.display.flip()
    vertices = []
    Init_input(vertices)
    default = vertices
    Draw(vertices)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    glTranslatef(0,0,5)

                if event.key == pygame.K_DOWN:
                    glTranslatef(0,0,-5)           

                if event.key == pygame.K_f:
                    vertices=func2d(vertices,default)


        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Line()
        Draw(vertices)
        pygame.display.flip()
        pygame.time.wait(10)


def main():
    f = input('Masukan Pilihan Input :')
    if f == '1':
        threeDimen()
    elif f == '2':
        twoDimen()
    else :
        quit()

main()