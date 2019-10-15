# Introduction to Programming
# Author: Reisha Puranik
# Date: October 15, 2019
def main():
    name = "dog"
    while True:
        print("The program is thinking of an animal")
        guess = input("Guess the name of the animal: ")
        if guess == "quit":
            print("You quit the game.")
            break
        elif guess.lower() == name.lower():
            print("Congratulations you guessed correctly! The animal name is dog")
            break
        else:
            print("Wrong guess. Please try again")
        
main()
