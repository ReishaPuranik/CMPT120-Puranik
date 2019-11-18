
# calculator.pyw
# Introduction to Programming Project 1
# Author: Reisha Puranik
# Date: October 11, 2019

# You should add comments to your code

# 11/17/2019: The calculator is not showing results.
# I cannot test the memory functions

from graphics import *
from calc_functions import *

def drawButton(button, win):
    x = button[0]
    y = button[1]
    label = button[2]
    width = button[3]

    # Create the rectangle for the button
    rect = Rectangle(Point(x + width/2, y - width/2),
                     Point(x - width/2, y + width/2))
    rect.draw(win)
    rect.setFill("lightblue")
    # Add the label
    text = Text(Point(x,y), label)
    text.draw(win)

def isButtonPressed(button, p):
    x = button[0]
    y = button[1]
    width = button[3]    
    return p.getX() + width/2 >= x and p.getX() - width/2 <= x \
           and p.getY() - width/2 <= y and p.getY() + width/2 >= y

def drawKeypad(buttons,win):
    for button in buttons:
        drawButton(button, win)

def getLabel(buttons, p):
    for button in buttons:
        if isButtonPressed(button,p):
            return button[2]

def solveEquation(equation):
    return 0

def buildEquation(equation,label):
    return ""

def displayEquation(equation,win): 
    while isButtonPressed == True:
        x1 = display[0]
        y2 = display[1]
        labl = display[2]
        widt = display[3]

        # Create the rectangle for the display
        aRectangle = Rectangle(Point(x + widt/2, y - widt/2),
                               Point(x - widt/2, y + widt/2))
        aRectangle.draw(win)
        aRecangle.setFill("lightgrey")
        # Add the label
        text = Text(Point(x1,y2), labl)
        text.draw(win)
    
def main():
    display = [[.5, 5.5, "", 1]]
    buttons = [[.5,4.5,'M+', 1],[1.5,4.5,'M-',1],[2.5,4.5,'MR',1],[3.5,4.5,'MC',1],
               [.5,.5,'+/-',1], [1.5,.5,'0',1],  [2.5,.5,'.',1],  [3.5,.5,'=',1],
               [.5,1.5,'1',1],  [1.5,1.5,'2',1], [2.5,1.5,'3',1], [3.5,1.5,'+',1],
               [.5,2.5,'4',1],  [1.5,2.5,'5',1], [2.5,2.5,'6',1], [3.5,2.5,'-',1],               
               [.5,3.5,'7',1],  [1.5,3.5,'8',1], [2.5,3.5,'9',1], [3.5,3.5,'*',1]]
    
    win = GraphWin('Calculator',400,600)
    win.setCoords(0, 0, 4, 6)
    drawKeypad(buttons, win)
    equation = ""
    display = ""
    M = ""
    while True:
        click = win.getMouse()
        label = getLabel(buttons,click)
        print(label)
        if label == '=':
            equation = solveEquation(equation)
            setText = buildEquation(equation,label)
        else:
            equation = buildEquation(equation,label)
        displayEquation(equation,display)
        
main()   
