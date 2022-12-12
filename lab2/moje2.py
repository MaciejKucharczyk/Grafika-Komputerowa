#!/usr/bin/env python3
from pickle import FALSE
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *
from random import random

x=-50.0
y=40.0
a=120
b=60
d=30 # stopien deformacji prostokata

R=0.0 
G=0.8
B=0.3

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass

"""
Funkcja rysuje prostokat
x,y - wspol. wierzcholka poczatkowego
a,b - wymiary prostokata
d - wspol deformacji
"""
def renderRectangleD(time, x, y, a, b, d):
    glClear(GL_COLOR_BUFFER_BIT)

    a+=d
    b+=d
   # glColor3f(0.0, 0.8, 0.3)
    glColor3f(random(), random(), random())
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(x+a, y)
    glVertex2f(x, y-b)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(x+a, y-b)
    glVertex2f(x+a, y)
    glVertex2f(x, y-b)
    glEnd()

    glFlush()

"""
Renderuje prostokat o danym kolorze
"""


def renderRectangle(time, x, y, a, b, R, G, B):

    glColor3f(R, G, B)
    glBegin(GL_TRIANGLES)
    glVertex2f(x, y)
    glVertex2f(x+a, y)
    glVertex2f(x, y-b)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(x+a, y-b)
    glVertex2f(x+a, y)
    glVertex2f(x, y-b)
    glEnd()

    glFlush()

"""def renderFractal2(time, x, y, a, b):
    glClear(GL_COLOR_BUFFER_BIT)

    for i in range (1, 10):
        renderRectangle(time, x, y, a, b, 1.0, 0.0, 0.0)
        renderRectangle(time, x+a/3, y-b/3, a/3, b/3, 1.0, 1.0, 1.0)

        renderRectangle(time, x+a/9, y-b/9, a/9, b/9, 1.0, 1.0, 1.0)
        renderRectangle(time, x+a/9, y-4*b/9, a/9, b/9, 1.0, 1.0, 1.0)
        renderRectangle(time, x+a/9, y-7*b/9, a/9, b/9, 1.0, 1.0, 1.0)

        renderRectangle(time, x+4*a/9, y-b/9, a/9, b/9, 1.0, 1.0, 1.0)
        renderRectangle(time, x+4*a/9, y-7*b/9, a/9, b/9, 1.0, 1.0, 1.0)

        renderRectangle(time, x+7*a/9, y-b/9, a/9, b/9, 1.0, 1.0, 1.0)
        renderRectangle(time, x+7*a/9, y-4*b/9, a/9, b/9, 1.0, 1.0, 1.0)
        renderRectangle(time, x+7*a/9, y-7*b/9, a/9, b/9, 1.0, 1.0, 1.0)

        a=a/3
        b=b/3



    glFlush()
    """


# Rekurencyjnie renderuje fraktal

def renderFractal(time, x, y, a, b):
   # glClear(GL_COLOR_BUFFER_BIT)

    renderRectangle(time, x, y, a, b, 1.0, 0.0, 0.0)
    renderRectangle(time, x+a/3, y-b/3, a/3, b/3, 1.0, 1.0, 1.0)
    if a<2:
        return
        
    a=a/3
    b=b/3

    renderFractal(time, x, y, a, b)
    renderFractal(time, x+a, y, a, b)
    renderFractal(time, x+2*a, y, a, b)
    renderFractal(time, x, y-b, a, b)
    renderFractal(time, x+2*a, y-b, a, b) 
    renderFractal(time, x, y-2*b, a, b)
    renderFractal(time, x+a, y-2*b, a, b)
    renderFractal(time, x+2*a, y-2*b, a, b)
    glFlush()

def renderTriangle(time):
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(0.0, 0.0)

    glColor3f(1.0, 0.0, 1.0)
    glVertex2f(0.0, 50.0)

    glColor3f(0.0, 1.0, 1.0)
    glVertex2f(-50.0, 0.0)
    glEnd()

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
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0,
                1.0, -1.0)

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
    glClear(GL_COLOR_BUFFER_BIT)
    while not glfwWindowShouldClose(window):
        renderFractal(glfwGetTime(), x, y, a, b)
        #renderRectangle(glfwGetTime(), x, y, a, b, R, G, B)
        #renderRectangleD(glfwGetTime(), x, y, a, b, d)
        #renderTriangle(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
