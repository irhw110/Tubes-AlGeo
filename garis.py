# Program menggambar garis

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

a=500
b=500
def draw():
	glColor3f(0.0,1.0,1.0)

	#Menggambar sumbu-X
	glBegin(GL_LINES)
	glVertex2f(-a,0)
	glVertex2f(a,0)
	glEnd()
	glutSwapBuffers()

	#Menggambar sumbu-Y
	glBegin(GL_LINES)
	glVertex2f(0,-a)
	glVertex2f(0,a)
	glEnd()
	glutSwapBuffers()


	v=input("X1=")
	w=input("Y1=")
	x=input("X2=")
	y=input("Y2=")

	#Menggambar garis
	glBegin(GL_LINES)
	glVertex2f(v,w)
	glVertex2f(x,y)
	glEnd()
	glutSwapBuffers()
	glutSwapBuffers()
	return


glutInit(sys.argv)
glutInitWindowPosition(0,0)
glutInitWindowSize(1000,1000)
glutCreateWindow("Kartesian")
glClearColor(1.0,1.0,1.0,0.0)
glOrtho(-a, a, -b, b, 0.0, 1.0)	# Bidang kartesian dengan rentang X dari -500 sampai 500 dan rentang Y dari -500 sampai 500
glutDisplayFunc(draw);
glutMainLoop();
