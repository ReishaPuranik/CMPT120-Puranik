# Introduction to Programming
# Author: Reisha Puranik
# Date: September 24, 2019
def main():
    n = eval(input("Enter an integer value: "))
    n1 = 1
    n2 = 1
    n3 = 1
    for i in range(3, n+1):
        n3 = n1+n2
        n1 = n2
        n2 = n3
    print(n3)
main()
