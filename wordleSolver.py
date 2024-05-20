#Imports
import random
import copy
from gameManager import gameManager

class wordleSolver:
    
    def __init__(self) -> None:
        
        self.wordBank = []

        #Open file
        f = open('wordBank.txt', 'r')
        lines = f.readlines()

        #Iterate through lines
        for line in lines:
            self.wordBank.append(line.strip("\n"))
            
        #Close file
        f.close()

        self.game = gameManager(self.wordBank)


    def naiveApproach(self):
        
        self.possibleWords = self.wordBank

        for i in range(0,5):
            guess = random.choice(self.possibleWords)
            self.game.guess(guess)
            self.naiveApproachHelper(guess)
            print(len(self.possibleWords))




    def naiveApproachHelper(self, guess):
        # Declarations
        letterIndex = 0
        dictonary = self.game.getKeys()
   
        possibleWords = copy.deepcopy(self.possibleWords)

        for letter in guess:
            key = dictonary.get(letter)
            removedWords = []

            if key.incorrectLetter:
                for word in possibleWords:
                    if letter in word:
                        removedWords.append(word)

                print("New length:", len(self.possibleWords))
            
       
            if key.correctLetter:
                for word in possibleWords:
                    if letter not in word:
                        removedWords.append(word)

                print("New length:", len(self.possibleWords))

            if key.correctSpot:
                for word in possibleWords:
                    if guess[letterIndex] != word[letterIndex]:
                        removedWords.append(word)

                print("New length:", len(self.possibleWords))

            letterIndex += 1

            # Remove words from self.possibleWords
            for word in removedWords:
                if (word not in self.possibleWords):
                    continue
                else:
                   self.possibleWords.remove(word)

#Driver function
if __name__ == '__main__':

    #Init solver
    solver = wordleSolver()

    solver.naiveApproach()






  


