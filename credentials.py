# CMPT 120 Intro to Programming
# Lab #4 – Working with Strings and Functions
# Author: Reisha Puranik
     # Created: 2019-10-01
def main():
    # get user's first and last names
    names = getnames()
    uname = username(names)
# TODO modify this to generate a Marist-style username uname = first + last
# ask user to create a new password
    passwd = getpassword()
    print("The force is strong in this one...")
    print("Account configured. Your new email address is", uname,"@marist.edu")


def getnames():
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    return [first,last]

def username(names):
     uname = names[0] + "." + names[1]
     return uname


def getpassword():
    passwd = input("Create a new password with at least 8 characters: ")    
    while not isStrong(passwd):
        print("Fool of a Took! That password is feeble!")
        passwd = input("Create a new password: ")
    return passwd

def isStrong(passwd):
    if len(passwd) < 8:
        return False
    if passwd.lower() == passwd:
        return False
    if passwd.upper() == passwd:
        return False
    return True

main()

    
