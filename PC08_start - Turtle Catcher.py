#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on WHAT DAY IS IT?

@author: jessicalieu

WHAT DOES YOUR GAME DO?
    OBJECTIVE - turtles will be running across the screen, and 
    you have to click as many turtles as you can before time runs out 
    
    RULES - you will get a score depending on how many turtles you click on 
    
    CHALLENGE - you will only be given 8 seconds to complete the task 
    
    INTERACTIONS - each time you click on turtle you get a point and the turtle 
    you click on is hidden 

"""

import turtle
import time, random

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 800
h = 800
panel.setup(width=w, height=h)
panel.bgcolor("DarkSeaGreen")

# ================ VARIABLE DEFINITION & SETUP =========================
running = True

# ================ FUNCTION DEFINITION =========================
# functions should go here IF they work with objects. 
# otherwise, try to include them in classes 

# ================ CLASSES =========================
class Movers:
    def __init__(self, x=-400, y=0):
        self.x = -400
        self.y = random.randint(-400,400)
        self.shape = turtle.Turtle(shape = 'turtle')
        self.shape.color("Beige")
        self.shape.up()
        self.shape.shapesize(3)
        self.shape.goto(self.x, self.y)
        # onclick functions get called here!
        self.shape.onclick(self.gotMe)
        self.shape.seth(0)
        
    # ======== METHODS DEFINITIONS ==========
    def walk(self):
        self.shape.forward(random.randint(3,20))
        if(self.shape.xcor() > 400):
            self.shape.goto(self.x, self.y)
        panel.update()
        
    def gotMe(self, x, y):
        self.count.update()
        self.shape.ht()
        print("Oh no! Not again!")
        
    def setCount(self, count):
        self.count = count 
        
class Count:
    def __init__(self):
        self.x = 300
        self.y = 330
        self.shape = turtle.Turtle(shape = 'circle')
        self.shape.up()
        self.shape.ht()
        self.shape.goto(self.x, self.y)
        self.count = 0 
        self.shape.write("POINTS: 0", font=("Verdona", 15, "bold"), align = "center")
        
    def update(self):
        self.shape.clear()
        self.count = self.count + 10
        self.shape.write ("POINTS: " +str (self.count), font=("Verdona", 15, "bold"), align = "center")
        
    def endGame(self):
        self.shape.goto(0,0)
        self.shape.color("red")
        self.shape.write("GAME OVER", font=("Verdona", 40, "bold"), align = "center")
    

# ================ OBJECTS =========================
count = Count()
instanceList = []
for i in range (9):
    temp = Movers()
    temp.setCount(count)
    instanceList.append(temp)
    
# ================ ANIMATION LOOP =========================
now = time.time() 
future = now + 8

while time.time() < future:
    
    for inst in instanceList:
        inst.walk()
        
    panel.update() # update the window with everything drawn in a single frame
    
    
# ================ CLEANUP =========================
print("Eng of Game")
count.endGame()
turtle.mainloop()  # allows for user interactions; handles cleanup

# ================ COMMENT =========================
"@keithkutsuma - more turtles to be added and time to increase when you click on the turtles, but it was a fun game!"
