import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

verticies = (
    (100, -100, -100),
    (100, 100, -100),
    (-100, 100, -100),
    (-100, -100, -100),
    (100, -100, 100),
    (100, 100, 100),
    (-100, -100, 100),
    (-100, 100, 100)
    )

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

def Cube():


    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()



def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, ((display[0])/display[1]), 0.1, 1000.0)
    glTranslatef(0,0,-500)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)


        Line()
        Cube()
        a = input()
        if a == 1 :
            glTranslatef(-1.0,1.0,0.0)
        elif a == 2 :
            glRotatef(45, 0, 0, 1)
        pygame.display.flip()



main()
