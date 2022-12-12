#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *
from random import random

a=100
x=-50.0
y=50

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass


def renderSquare(time, x, y, a):
    color1 = random()
    color2 = random()
    glBegin(GL_TRIANGLES)
    glColor3f(random(), 1.0, 1.0)
    glVertex2f(x, y)
    glColor3f(color1, 1.0, 1.0)
    glVertex2f(x+a, y)
    glColor3f(color2, 1.0, 1.0)
    glVertex2f(x, y-a)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(random(), 1.0, 1.0)
    glVertex2f(x+a, y-a)
    glColor3f(color1, 1.0, 1.0)
    glVertex2f(x+a, y)
    glColor3f(color2, 1.0, 1.0)
    glVertex2f(x, y-a)
    glEnd() 

    glFlush()   

def renderPlasmaFractal(time, x, y, a):
    # glClear(GL_COLOR_BUFFER_BIT)
    renderSquare(time, x, y, a)
    a=a/2

   # renderSquare(time, x, y, a)
   # renderSquare(time, x+a, y, a)
    # renderSquare(time, x, y-a, a)
    #renderSquare(time, x+a, y-a, a)

    if a<2:
        return

    renderPlasmaFractal(time, x, y, a)
    renderPlasmaFractal(time, x+a, y, a)
    renderPlasmaFractal(time, x, y-a, a)
    renderPlasmaFractal(time, x+a, y-a, a)

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
        renderPlasmaFractal(glfwGetTime(), x, y, a)
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
