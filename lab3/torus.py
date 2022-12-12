#!/usr/bin/env python3
from cmath import cos, pi, sin
import math
from random import random
import sys
import numpy

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *

N = 40

r = 1.5
R = 3.0

color1 = [random(), random(), random()]
color2 = [random(), random(), random()]
color3 = [random(), random(), random()]
color4 = [random(), random(), random()]


wierzcholki = numpy.zeros((N, N, 3))
u = [0]*N
v = [0]*N

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)


def shutdown():
    pass


def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)

    glEnd()

def spin(angle):
    glRotatef(angle, 1.0, 0.0, 0.0)
    glRotatef(angle, 0.0, 1.0, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)

def eggStripes(wierzcholki):
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(N):
        for j in range(N):
            glColor3f(color1[0], color1[1], color1[2])
            glVertex3f(wierzcholki[i][j][0], wierzcholki[i][j][1], wierzcholki[i][j][2]) # i,j
            glColor3f(color2[0], color2[1], color2[2])
            glVertex3f(wierzcholki[(i+1)%N][j][0], wierzcholki[(i+1)%N][j][1], wierzcholki[(i+1)%N][j][2]) #i+1, j

            glColor3f(color3[0], color3[1], color3[2])
            glVertex3f(wierzcholki[i][(j+1)%N][0], wierzcholki[i][(j+1)%N][1], wierzcholki[i][(j+1)%N][2]) #i, j+1
            glColor3f(color4[0], color4[1], color4[2])
            glVertex3f(wierzcholki[(i+1)%N][(j+1)%N][0], wierzcholki[(i+1)%N][(j+1)%N][1], wierzcholki[(i+1)%N][(j+1)%N][2]) # i+1, j+1
    glEnd()

def torus():
    for i in range(N):
        u[i]=i/(N-1)
        v[i]=i/(N-1)

    for i in range(N):
        for j in range(N):
            wierzcholki[i][j][0] = (R + r*math.cos(2*pi*v[j]))*math.cos(2*pi*u[i])       # wspolrzedna x
            wierzcholki[i][j][1] = (R + r*math.cos(2*pi*v[j]))*math.sin(2*pi*u[i])       # wspolrzedna y
            wierzcholki[i][j][2] = r*math.sin(2*pi*v[j])                                 # wspolrzedna z

    """
    Ponizsze funkcja generuja torus
    """
    eggStripes(wierzcholki)


def render(time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    axes()

    angle = time*(180/pi)
    spin(angle)

    torus()

    glFlush()


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-7.5, 7.5, -7.5 / aspect_ratio, 7.5 / aspect_ratio, 7.5, -7.5)
    else:
        glOrtho(-7.5 * aspect_ratio, 7.5 * aspect_ratio, -7.5, 7.5, 7.5, -7.5)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
