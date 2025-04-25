import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
import turtle
import math as ma
import random
import time
import keyboard

sw = 800  
sh = 600
d=100
v=5
wn = turtle.Screen()
wn.setup(width = sw, height = sh)
wn.title("Vector Graphics Demo by TokyoEdTech")
wn.bgcolor("black")
wb=10
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
P=np.array([0,0,0])
V=wb*np.array([np.array([-10,-10,d]),np.array([10,-10,d]),np.array([-10,10,d]),np.array([10,10,d]),
               np.array([-9,-9,d]),np.array([9,-9,d]),np.array([-9,9,d]),np.array([9,9,d])])
th=0
tv=0
tV=V
E=[[0,1],[1,3],[3,2],[2,0],[4,5],[5,7],[7,6],[6,4]]
def forward():
    global P
    for i in V:
        i+=[0,0,-v]
    render()
def back():
    global P
    for i in V:
        i+=[0,0,v]
    render()
def sleft():
    global P
    for i in V:
        i+=[v,0,0]
    #print(P)
    render()
def sright():
    global P
    for i in V:
        i+=[-v,0,0]
    #print(P)
    render()
def lleft():
    global tV
    global th
    th-=ma.pi/20
    tV=[]
    Rot=np.array([[ma.cos(th),ma.sin(th),0],[-ma.sin(th),ma.cos(th),0],[0,0,1]])
    for i in V:
        tV.append(np.matmul(Rot,i))
    #print(P)
    render()
def lright():
    global tV
    global th
    th+=ma.pi/20
    tV=[]
    Rot=np.array([[ma.cos(th),ma.sin(th),0],[-ma.sin(th),ma.cos(th),0],[0,0,1]])
    for i in V:
        #print(i)
        i=np.matmul(Rot,i)
        #print(i)
    #print(P)
    render()
def lup():
    global tV
    global tv
    tv+=ma.pi/20
    tV=[]
    Rot=np.array([[ma.cos(tv),0,ma.sin(tv)],[0,1,0],[-ma.sin(tv),0,ma.cos(tv)]])
    for i in V:
        i=np.matmul(Rot,i)
    #print(P)
    render()
pen.penup()
pen.width(2)
wn.tracer(0)
def render(): # Draw each line
    pen.clear()
    PV=[]
    PC=[]
    per=[]
    j=0
    for i in V:
        per0=np.arctan(i[1]/np.linalg.norm([i[0],i[2]]))
        per1=np.arctan(i[0]/i[2])
        PC.append([d*sw*per1,d*sh*per0])
        PV.append([abs(per1)*sw*np.sign(i[0]),abs(per0)*sh*np.sign(i[1])])
        #print(i[2])
    for i in E:
        j+=1
        pen.goto(PV[i[0]][0],PV[i[0]][1])
        pen.down()
        pen.goto(PV[i[1]][0],PV[i[1]][1])
        pen.up()
        if j<5:
            pen.goto(PV[i[0]][0],PV[i[0]][1])
            pen.down()
            pen.goto(PC[i[0]][0],PC[i[0]][1])
            pen.up()
        '''
while True:
        
    # Clear the screen
    pen.clear()

    # Update objects
    for enterprise in enterprises:
        enterprise.move(SCREEN_WIDTH, SCREEN_HEIGHT)
        enterprise.render(pen)

    # Update the screen
    wn.update()
'''
render()
#forw = Button(screen, text="Forward", command=lambda:forward())  # Creating button
keyboard.on_press_key("'", lambda _:sleft())
keyboard.on_press_key(".", lambda _:sright())
keyboard.on_press_key(",", lambda _:forward())
keyboard.on_press_key("o", lambda _:back())
keyboard.on_press_key("a", lambda _:lleft())
keyboard.on_press_key("e", lambda _:lright())
wn.mainloop()
