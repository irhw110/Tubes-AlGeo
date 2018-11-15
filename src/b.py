from OpenGL.GL import*
from OpenGL.GLUT import*
from OpenGL.GLU import*
from tr2d import *
import numpy as np
import serial
import os
import threading
import sys
import time

global vertices

a=500
b=500
def draw(v,w,x,y):
	#Menggambar garis
	glColor2f(0.0,0.0,1.0)
	glBegin(GL_LINES)
	glVertex2f(v,w)
	glVertex2f(x,y)
	glEnd()
	glutSwapBuffers()
	return

def init() :
	#Menggambar sumbu-X
	glColor3f(0.0,0.0,1.0)
	glBegin(GL_LINES)
	glVertex3f(-a,0,0)
	glVertex3f(a,0,0)
	glEnd()
	glutSwapBuffers()

	#Menggambar sumbu-Y
	glBegin(GL_LINES)
	glVertex3f(0,-a,0)
	glVertex3f(0,a,0)
	glEnd()
	glutSwapBuffers()
	return

def display():

    glBegin(GL_TRIANGLES)
    glVertex2fv(vertices[0][0],vertices[0][1])
    glVertex2fv(vertices[1][0],vertices[1][1])
    glVertex2fv(vertices[2][0],vertices[2][1])
    glEnd()
    glutSwapBuffers()


# Main
glutInit(sys.argv)
glutInitWindowPosition(0,0)
glutInitWindowSize(1000,1000)
glutCreateWindow("Kartesian")
glClearColor(1.0,1.0,1.0,0.0)	# Bidang kartesian dengan rentang X dari -500 sampai 500 dan rentang Y dari -500 sampai 500
init()
vertices = [[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]

glOrtho(-a, a, -b, b, 0.0, 1.0)
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
glLoadIdentity()
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45.0, float(600)/float(600), 0.1, 100.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glTranslatef(0.0,0.0,-6.0)
init()
glBegin(GL_TRIANGLES)
glVertex3f(0,0,0)
glVertex3f(200,100,0)
glVertex3f(100,200,0)
glEnd()
glutSwapBuffers()

glutMainLoop()
