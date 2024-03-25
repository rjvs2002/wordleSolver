#Imports
import random


class cell():
    def __init__(self) -> None:
        self.content = " "

        self.correctSpot = False
        self.correctLetter = False
        self.incorrectLetter = False

        #Block colors
        self.reset = '\033[0m'
        self.correctSpotColor = '\033[48;5;82m'
        self.correctLetterColor = '\033[48;5;226m'
        self.incorrectLetterColor = '\033[48;5;246m'


    def __str__(self):

        if self.correctSpot == True:
            return(self.correctSpotColor + "[" + self.content  +']' + self.reset)
        
        if self.correctLetter == True:
            return(self.correctLetterColor + "[" + self.content  +']' + self.reset)
        
        if self.incorrectLetter == True:
            return(self.incorrectLetterColor + "[" + self.content  +']' + self.reset)
        
        return("[" + self.content + ']')


class board():

    def __init__(self) -> None:
        
        self.rows = 5
        self.columns = 5
        self.grid = [[0 for x in range(5)] for y in range(5)] 

        for row in range (self.rows):
            for col in range (self.columns):
                self.grid[row][col] = cell()
    

    def printer(self):
        
        for row in  range (self.rows):
            for col in  range (self.columns):
                print (self.grid[row][col], end='')
            print("")



class keys():

    def __init__(self) -> None:
        ['q','w','e','r','t','y','u','i','o','p']
        ['a','s','d','f','g','h','j','k','l']
        ['z','x','c','v','b','n','m']
        
        pass




class gameManager():
    
    def __init__(self) -> None:

        self.guessCount = 0
        
        #Initalize list
        self.wordBank = []

        #Open file
        f = open('wordBank.txt', 'r')
        lines = f.readlines()

        #Iterate through lines
        for line in lines:
            self.wordBank.append(line.strip("\n"))
            
        #Close file
        f.close()

        #Select word
        self.selectedWord = random.choice(self.wordBank)
        print(self.selectedWord)

        #Initialize board
        self.boardObject = board()
        self.grid = self.boardObject.grid
       
    def guess(self, guessIn):
        
        
        for i in range(5):

            #Update letter in cell
            self.grid[self.guessCount][i].content = guessIn[i]

            #Check if in correct spot
            if guessIn[i] == self.selectedWord[i]:
                self.grid[self.guessCount][i].correctSpot = True

            elif self.correctLetter(guessIn[i]):
                self.grid[self.guessCount][i].correctLetter = True

            else:
                self.grid[self.guessCount][i].incorrectLetter = True

        self.guessCount += 1


        self.boardObject.printer()

      
                        




    #Check if a correct letter
    def correctLetter(self, charIn):
        if charIn in self.selectedWord:
            return True
        return False
        
    





    

 