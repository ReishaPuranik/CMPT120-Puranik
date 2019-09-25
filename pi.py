# Introduction to Programming
# Author: Reisha Puranik
# Date: September 24, 2019
import math
def main():
    n = int(input("Enter a value:"))
    total = 0
    for i in range(1, n):
        total += (-1)**(i+1)*((1.0/(i+i+1)))
    num = 4*(1-total)
    print(num)

    print("The approximation of the value is:",((num) - (math.pi)), "away from pi")
main()
