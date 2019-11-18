# Introduction to Programming
# Author: Reisha Puranik
# Date: November 12, 2019

# JA: Always remember to add comments to your code

class Product:
    

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def isinStock(self, count):
        return self.quantity >= count

    def cost(self, count):
        return self.price * count

    def reduceStock(self, count):
        self.quantity = self.quantity - count
    
    
products = [(Product("Ultrasonic range finder", 2.50, 4)),
            (Product("Servo motor", 14.99, 10)),
            (Product("Servo controller", 44.95, 5)),
            (Product("Microcontroller Board", 34.95, 7)),
            (Product("Laser range finder", 149.99, 2)),
            (Product("Lithium polymer battery", 8.99, 8))]

                  
def printStock():
    print()
    print("Available Products")
    print("------------------")
    i = 0
    for product in products:
        if product.isinStock(1):
            print(str(i)+")",product.name, "$", product.price)
            i = i + 1


def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit": break
        prodId = int(vals[0])
        count = int(vals[1])
        product = products[prodId]
        if product.isinStock(count):
            if cash >= product.cost(count):
                product.reduceStock(count)
                cash -= product.cost(count)
                print("You purchased", count, product.name +".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", product.name)
main()
