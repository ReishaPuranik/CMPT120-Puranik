# Introduction to Programming Project 1
# Author: Reisha Puranik
# Date: October 11, 2019

def calculator():
    mylist = input("Enter equation to be solved: ").split()
    while len(mylist) > 1:
        if "/" in mylist:
            index = mylist.index('/')
            num1 = float(mylist[index - 1])
            num2 = float(mylist[index + 1])
            del(mylist[index-1:index+2])
            mylist.insert(index - 1, num1/num2)
            print(mylist)
        elif "*" in mylist:
            index = mylist.index('*')
            num1 = float(mylist[index - 1])
            num2 = float(mylist[index + 1])
            del(mylist[index-1:index+2])
            mylist.insert(index - 1, num1*num2)
            print(mylist)
        elif "+" in mylist:
            index = mylist.index('+')
            num1 = float(mylist[index - 1])
            num2 = float(mylist[index + 1])
            del(mylist[index-1:index+2])
            mylist.insert(index - 1, num1+num2)
            print(mylist)
        elif "-" in mylist:
            index = mylist.index('-')
            num1 = float(mylist[index - 1])
            num2 = float(mylist[index + 1])
            del(mylist[index-1:index+2])
            mylist.insert(index - 1, num1-num2)
            print(mylist)
        else:
            print("Invalid operation")
        
        

calculator()



    
        
