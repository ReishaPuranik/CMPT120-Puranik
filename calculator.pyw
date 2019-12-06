# calculator.pyw
# Introduction to Programming Project 1
# Author: Reisha Puranik
# Date: October 11, 2019

from graphics import *
from calc_functions import *

#This is the button class that creates functionality of the buttons 
class Button:
    def __init__(self, x, y, label, width, win):
        self.x = x
        self.y = y
        self.label = label
        self.win = win
        self.width = width

        #Creates the rectangle for the buttons
        self.rect = Rectangle(Point(x + width/2, y - width/2),
                              Point(x - width/2, y + width/2))
        self.rect.draw(win)
        self.rect.setFill("lightblue")
       
        self.text = Text(Point(x,y), label)
        self.text.draw(win)

    def isButtonPressed(self, button, p):
        self.x = button[0]
        self.y = button[1]
        self.width = button[3]    
        return p.getX() + width/2 >= x and p.getX() - width/2 <= x \
               and p.getY() - width/2 <= y and p.getY() + width/2 >= y


    def getLabel(buttons, p):
        for button in buttons:
            if isButtonPressed(button,p):
                return button[2]

#This is the display class that adds color and text of the buttons on the calculator
class Display:
    def __init__(self, win, display):
        self.win = win
        self.rect = Rectangle(Point(0.1, 6.9),Point(3.9,4.1))
        self.rect.setFill("lightgray")
        self.rect.draw(win)
        self.display = Text(Point(.5, 6.5), "")
        self.display.setSize(20)
        self.display.setStyle("bold")
        self.display.draw(win)
        self.display.setText(equation.rjust(50))      


#This is the calculator class that sets the window for the actual calculator
class Calculator:
    def __init__(self):
        self.win = GraphWin("Calculator",600, 400)
        self.win.setCoords(0, 0, 4, 7)
        self.win.setBackground("lightblue")
        width = .5
        #This is where the actual buttons are made
        self.buttons = [Button(.5,4.5,'M+', width,self.win),Button(1.5,4.5,'M-',width,self.win),Button(2.5,4.5,'MR',width, self.win),Button(3.5,4.5,'MC',width, self.win),
                        Button(.5,.5,'+/-',width, self.win), Button(1.5,.5,'0',width,self.win),  Button(2.5,.5,'.',width,self.win),  Button(3.5,.5,'=',width,self.win),
                        Button(.5,1.5,'1',width,self.win),  Button(1.5,1.5,'2',width,self.win), Button(2.5,1.5,'3',width,self.win), Button(3.5,1.5,'+',width,self.win),
                        Button(.5,2.5,'4',width,self.win),  Button(1.5,2.5,'5',width,self.win), Button(2.5,2.5,'6',width,self.win), Button(3.5,2.5,'-',width,self.win),               
                        Button(.5,3.5,'7',width,self.win),  Button(1.5,3.5,'8',width,self.win), Button(2.5,3.5,'9',width,self.win), Button(3.5,3.5,'*',width,self.win)]
        self.equation = ""
        
    def solveEquation(equation):
        return ""

    def buildEquation(self, equation,label):
        if label in ["+", "-", "*", "/"]:
            self.equation += " " + label + " "
        elif label not in ["M+", "M-", "MR", "MC"]:
            self.equation += label
        return equation

    #This is the memory for the calculator 
    def processMemory(self, label, equation):
        #Adds the last result to memory
        if label == 'M+':
            self.memory = memory + solveEquation(equation)
            return solveEquation(equation)
        #Subtracts the last result from memory
        elif label == "M-":
            self.memory = memory - solveEquation(equation)
            return solveEquation(equation)
        #Recalls the value from memory
        elif label == "MR":
            return equation + str(memory)
        #This will clear the memory
        else:
           self.memory = 0
           return equation
        
    def drawKeypad(self, buttons,win):
        for button in buttons:
            button.drawButton(win)

    def run(self):
        self.win, display, buttons = self.Calculator()
        
              
def main():
    calc = Calculator()
    calc.run()
main()   
