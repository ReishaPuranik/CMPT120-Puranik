def introduction():
    pass

#Gets the mode of interaction from the user
def nextInteraction():
    print("Select your action:")
    print(" 0 - reward, 1 - punish, 2 - threaten, 3 - joke")
    action = int(input("Make your selection:"))
    return action

#First row is anger, second row is disgust, third is fear, fourth is happiness, fifth is sadness, and sixth is surprise
#First column is reward, second is punish, third is threaten, and fourth is joke
#Looks up emotion and determines next emotional state
def lookupEmotion(currentState, action):
    emotionmatrix = [[3, 0, 1, 1], 
                     [1, 0, 0, 1], 
                     [5, 2, 2, 4], 
                     [3, 5, 1, 3], 
                     [3, 4, 2, 3], 
                     [3, 4, 5, 5]]
                    
    return emotionmatrix[currentState][action]

#Prints phrases of emotions
def showEmotion(currentState):
    phrases = ["I'm angry", "I'm disgusted", "I'm scared", "I'm so happy", "I'm depressed", "I'm shocked"]
    print(phrases[currentState])

               
def main():
    introduction()
    currentState = 3
    while True:
        action = nextInteraction()
        currentState = lookupEmotion(currentState, action)
        showEmotion(currentState)
        
main()
