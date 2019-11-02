# Introduction to Programming Project 1
# Author: Reisha Puranik
# Date: October 11, 2019

from calc_functions import * 
from graphics import *
          

def checkButton(point):
    for coord in coords:
        index = inside(coord)
        if index == 1:
            return (label[index])

def createGui(win, coords, labels):
    for row in coords:
        rowIndex = coords.index(row)
        for button in row:
            colIndex = row.index(button)
            aRectangle = Rectangle(Point(button[0]-15, button[1] - 15),  Point(button[0]+15, button[1]+15))
            aRectangle.setFill("lightblue")
            aRectangle.draw(win)
            Text(Point(button[0],button[1]),labels[rowIndex][colIndex]).draw(win)
        

def getLabel(click, coords, labels):
    for row in coords:
        for col in row:
            if click.getX() >= col[0] - 15 and click.getX() <= col[0] + 15 and click.getY() >= col[1] -15 and click.getY() <= col[1] + 15:
                return labels[coords.index(row)][row.index(col)]

def display(win, displayCoords):
    display = Rectangle(Point(0, 0), Point(125, 50)).draw(win)
    display.setFill("grey")
    
def main():
    win = GraphWin("Calculator", 150, 250)
    win.setBackground("white")
    coords = [[[20,50], [55, 50], [90,50], [125,50]],
              [[20,85], [55, 85], [90,85], [125,85]],
              [[20,120],[55,120], [90,120],[125,120]],
              [[20,155],[55,155], [90,155],[125,155]],
              [[20,190],[55,190], [90,190],[125,190]]]
    
    labels = [["7", "8", "9", "/"],
              ["4", "5", "6", "*"],
              ["1", "2", "3", "+"],
              ["+/-", "0", ".", "-"],
              [" ", " ", "Del", "="]]
    
    
    createGui(win, coords, labels)
    while True:
        click = win.getMouse()
        label = getLabel(click, coords, labels)
        print(label)

    display(win, displayCoords)
    while True:
        eq = solve(eqStr)
        text.setText(solve(eqStr))
           
        
        
    
    
        
main()



            
