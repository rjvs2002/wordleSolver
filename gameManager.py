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
    
    def __str__(self):
        for row in  range (self.rows):
                    for col in  range (self.columns):
                        print (self.grid[row][col], end='')
                    print("")

        return ("")

class keys():

    def __init__(self) -> None:
        self.topRow = ['q','w','e','r','t','y','u','i','o','p']
        self.midRow = ['a','s','d','f','g','h','j','k','l']
        self.bottomRow = ['z','x','c','v','b','n','m']

        self.rows = [self.topRow,self.midRow,self.bottomRow]


        self.keyBoard = {}

        for row in self.rows: 
            for letter in row:
                self.keyBoard[letter] = cell()
                self.keyBoard[letter].content = letter


    def updateKey(self,keyIn,input):
        match input:
            case "incorrectLetter":
                self.keyBoard[keyIn].incorrectLetter = True
                self.keyBoard[keyIn].correctLetter = False
                self.keyBoard[keyIn].correctSpot = False
            case "correctLetter":
                self.keyBoard[keyIn].correctLetter = True
                self.keyBoard[keyIn].correctSpot = False
                self.keyBoard[keyIn].incorrectLetter = False
            case "correctSpot":
                self.keyBoard[keyIn].correctSpot = True
                self.keyBoard[keyIn].correctLetter = False
                self.keyBoard[keyIn].incorrectLetter = False

    def __str__(self):
        print("_________________________________")

        for row in self.rows:
            for letter in row:
                print (self.keyBoard[letter], end='')
            print("")

        return "_________________________________"

class gameManager():
    
    def __init__(self,wordBank) -> None:

        self.guessCount = 0
        
        #Initalize list
        self.wordBank = wordBank

        #Select word
        self.selectedWord = random.choice(self.wordBank)
        print(self.selectedWord)

        #Initialize board
        self.boardObject = board()
        self.grid = self.boardObject.grid

        #Initalize keys
        self.keyBoard = keys()
        print(self.keyBoard)


    #Take a guess   
    def guess(self, guessIn):
        
        

        #Iterate through cells
        for i in range(5):

            #Update letter in cell
            self.grid[self.guessCount][i].content = guessIn[i]

            #Check if in correct spot
            if guessIn[i] == self.selectedWord[i]:
                self.grid[self.guessCount][i].correctSpot = True
                self.keyBoard.updateKey(guessIn[i], "correctSpot" )
                
            elif self.correctLetter(guessIn[i]):
                self.grid[self.guessCount][i].correctLetter = True
                self.keyBoard.updateKey(guessIn[i], "correctLetter" )
           

            else:
                self.grid[self.guessCount][i].incorrectLetter = True
                self.keyBoard.updateKey(guessIn[i], "incorrectLetter" )
      
        self.guessCount += 1


        #self.boardObject.printer()
        print(self.boardObject)
        print(self.keyBoard)


    def getKeys(self):
        return self.keyBoard.keyBoard


    def reset(self):
        #Initialize board
        self.boardObject = board()
        self.grid = self.boardObject.grid

        #Initalize keys
        self.keyBoard = keys()

        #Reset guessCount
        self.guessCount = 0


    #Check if a correct letter
    def correctLetter(self, charIn):
        if charIn in self.selectedWord:
            return True
        return False
        
    





    

 