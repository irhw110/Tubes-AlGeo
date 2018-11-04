# Program menggambar garis

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

a=500
b=500
def draw(v,w,x,y):
	#Menggambar garis
	glColor3f(0.0,0.0,1.0)
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
	return

def display():

	init()
	glTranslatef(100,100,0)
	draw(r,s,t,u);

	glutSwapBuffers()


# Main
glutInit(sys.argv)
glutInitWindowPosition(0,0)
glutInitWindowSize(1000,1000)
glutCreateWindow("Kartesian")
glClearColor(1.0,1.0,1.0,0.0)
glOrtho(-a, a, -b, b, 0.0, 1.0)	# Bidang kartesian dengan rentang X dari -500 sampai 500 dan rentang Y dari -500 sampai 500

init()
r=input("X1=")
s=input("Y1=")
t=input("X2=")
u=input("Y2=")
draw(r,s,t,u)

d=input("Masukkan d :")
if d== 1 :
	glutDisplayFunc(display)
	glutMainLoop();



#A=input("Pilih metode :")
#whileA != 0:
#	if A==1 :
#glTranslatef(100,100,0)
