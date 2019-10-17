# Introduction to Programming Project 1
# Author: Reisha Puranik
# Date: October 11, 2019


def main():
    mylist = input("Enter equation to be solved: ").split()
    while len(mylist) > 1:
        #This operation divides numbers
        if "/" in mylist:
            index = mylist.index('/')
            num1 = float(mylist[index - 1])
            num2 = float(mylist[index + 1])
            del(mylist[index-1:index+2])
            mylist.insert(index - 1, num1/num2)
            print(mylist)
        #This operation multiplies numbers
        elif "*" in mylist:
            index = mylist.index('*')
            num1 = float(mylist[index - 1])
            num2 = float(mylist[index + 1])
            del(mylist[index-1:index+2])
            mylist.insert(index - 1, num1*num2)
            print(mylist)
        #This operation adds numbers
        elif "+" in mylist:
            index = mylist.index('+')
            num1 = float(mylist[index - 1])
            num2 = float(mylist[index + 1])
            del(mylist[index-1:index+2])
            mylist.insert(index - 1, num1+num2)
            print(mylist)
        #This operation subtracts numbers
        elif "-" in mylist:
            index = mylist.index('-')
            num1 = float(mylist[index - 1])
            num2 = float(mylist[index + 1])
            del(mylist[index-1:index+2])
            mylist.insert(index - 1, num1-num2)
            print(mylist)
        else:
            print("Invalid operation")
            
main()


