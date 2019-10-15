# Introduction to Programming
# Author: Reisha Puranik
# Date: October 15, 2019
def main():
    name = "dog"
    while True:
        print("The program is thinking of an animal")
        guess = input("Guess the name of the animal: ")
        if guess != name:
            print("Wrong guess. Please try again")
        else:
            print("Congratulations you guessed correctly! The animal name is dog")
            break
        
main()
