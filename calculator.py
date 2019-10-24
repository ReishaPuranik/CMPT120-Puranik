# Introduction to Programming Project 1
# Author: Reisha Puranik
# Date: October 11, 2019

from calc_functions import * 
import graphics 

def main():
    str = input("Enter equation: ")
    print(solve(str))

main()

def __init__(self):
    win = GraphWin("Calculator")
    win.setCoords(0, 0, 6, 7)
    win.setBackground("slategray")
    self.win = win
    bSpecs = [(2,1,'0'), (3,1,'.'),
              (1,2,'1'), (2,2,'2'), (3,2,'3'), (4,2,'+'), (5,2,'-'),
              (1,3,'4'), (2,3,'5'), (3,3,'6'), (4,3,'*'), (5,3,'/'),
              (1,4,'7'), (2,4,'8'), (3,4,'9'), (4,4,'<-'),(5,4,'C')]
    self.buttons = []
    for (cx, cy, label) in bSpecs:
        self.buttons.append(Button(self.win,Point(cx, cy),
                                   .75,.75,label))
        self.buttons.append(Button(self.win, Point(4.5,1),
                                   1.75, .75, "="))
        for b in self.buttons:
            b.activate()
        for (cx,cy,label) in bSpecs:
            
            
