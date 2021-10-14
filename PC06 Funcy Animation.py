#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on WHAT DAY IS IT???

@author: WHO ARE YOU??

WHAT DOES YOUR CODE DO???
"""

import turtle

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) 
turtle.tracer(0) 

panel = turtle.Screen()
w = 700
h = 500
panel.setup(width=w, height=h)
panel.bgcolor("orange")

# ================ VARIABLE DEFINITION & SETUP =========================
pumpkin = turtle.Turtle(shape="circle")
size = 6
running = True
step = 1
count = 0
crosses = 10

yvel = 4 #movement variables for y axis
yacc = -0.2 #movement variables for y axis

pumpkinImg = "pumpkingif.gif"
panel.register_shape(pumpkinImg)
pumpkin.shape(pumpkinImg)


# ================ FUNCTION DEFINITION =========================
def star():
    '''draws a star'''
    pumpkin.color("black")
    for i in range(5):
        pumpkin.forward(100)
        pumpkin.right(144)
def movement(yvel, yacc): #getting the x and y position
    xpos = pumpkin.xcor()
    ypos = pumpkin.ycor()
    pumpkin.forward(4) 
    pumpkin.sety(ypos + yvel) 
    if xpos >= w/2:
        pumpkin.goto(-w/2,ypos)
    
    # return changed values of y speed
    if ypos < 0:
        return 4
    else:
        return yvel + yacc
    
# ================ ANIMATION LOOP =========================

while running:
    star()
    yvel = movement(yvel, yacc)
    panel.update()
          
# ================ CLEANUP =========================
turtle.done()



