#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.up()
turtle.goto(0,0)
turtle.goto(-30,10)
turtle.color("orange")
turtle.begin_fill()
turtle.down()
turtle.circle(100)
turtle.end_fill()
turtle.up()
turtle.goto(30,10)
turtle.begin_fill()
turtle.down()
turtle.circle(100)
turtle.end_fill()
turtle.up()
turtle.color("black")
turtle.begin_fill()
turtle.goto(-70,108)
turtle.down()
turtle.forward(40)
turtle.left(120)
turtle.forward(40)
turtle.left(120)
turtle.forward(40)
turtle.end_fill()
turtle.up()
turtle.begin_fill()
turtle.goto(30,108)
turtle.left(120)
turtle.down()
turtle.forward(40)
turtle.left(120)
turtle.forward(40)
turtle.left(120)
turtle.forward(40)
turtle.end_fill()
turtle.up()
turtle.goto(-10,84)
turtle.left(120)
turtle.down()
turtle.pensize(5)
turtle.forward(30)
turtle.left(120)
turtle.forward(30)
turtle.left(120)
turtle.forward(30)
turtle.up()
turtle.goto(-40,50)
turtle.pensize(0)
turtle.left(120)
turtle.down()
turtle.begin_fill()
turtle.forward(90)
turtle.left(40)
turtle.forward(25)
turtle.left(150)
turtle.forward(90)
turtle.end_fill()
turtle.up()
turtle.begin_fill()
turtle.goto(-40,50)
turtle.down()
turtle.left(300)
turtle.forward(20)
turtle.left(215)
turtle.forward(60)
turtle.end_fill()

turtle.up()
turtle.pensize(20)
turtle.color("green")
turtle.goto(-20,190)
turtle.down()
turtle.begin_fill()
turtle.forward(30)
turtle.left(50)
turtle.forward(30)
turtle.left(70)
turtle.forward(50)
turtle.left(70)
turtle.forward(30)
turtle.left(70)
turtle.forward(50)
turtle.left(70)
turtle.forward(30)
turtle.end_fill()













#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
