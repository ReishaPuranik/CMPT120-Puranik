# Introduction to Programming
# Author: Reisha Puranik
# Date: October 15, 2019
def main():
    name = "dog"
    while True:
        print("The program is thinking of an animal")
        guess = input("Guess the name of the animal: ")
        if guess[0] == "q":
            print("You quit the game.")
            break
        elif guess.lower() == name.lower():
            print("Congratulations you guessed correctly! The animal name is dog")
            favor=input("Do you like this animal?:")
            if favor == "y":
                print("me too")
            if favor == "n":
                print("Aw ok")
            break   
        else:
            print("Wrong guess. Please try again")
        
main()
