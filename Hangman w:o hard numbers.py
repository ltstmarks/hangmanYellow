#This is my awesome (non-violent) hangman game!

from turtle import *
from random import randint
import time
import math

wordBank = ['awkward', 'absurd', 'avenue', 'abyss', 'bagpipes', 'banjo',\
            'beekeeper','bikini', 'blizzard', 'boggle', 'bookworm', 'boxcar',\
            'buckaroo', 'bungler','buzzing', 'cobweb', 'cockiness', 'crypt',\
            'cycle', 'dizzying', 'dwarves','embezzle', 'faking', 'fishhook',\
            'fluffiness', 'frazzled', 'fuchsia', 'funny','galaxy', 'gazebo',\
            'glowworm', 'gnarly', 'gnat', 'gypsy', 'haiku', 'haphazard',\
            'ivory', 'jackpot', 'jawbreaker', 'jazzy', 'jigsaw', 'jukebox',\
            'kayak', 'kahki', 'kazoo', 'keyhole', 'kiosk', 'length', 'lucky',\
            'luxury','matrix', 'memento', 'microwave', 'mystify', 'oxygen',\
            'pajamas', 'peekaboo','pixel','polka', 'puppy', 'puzzling',\
            'quartz', 'quiz', 'rhubarb','rhythmic', 'rogue', 'scratch',\
            'strength', 'subway', 'swivel', 'transcript', 'transplant',\
            'unknown', 'unzip', 'waxy', 'wavy', 'wildebeest', 'witchcraft',\
            'wizard', 'yacht', 'zigzag', 'zodiac', 'zombie']

sWidth = 600
sHeight = 800
s = getscreen()
s.setup(sWidth, sHeight)
s.bgcolor('#aafff8')

t=getturtle()
t.color('#8d71fc')
t.width(6)
t.speed(0)

# variables for use across all functions
nooseX = None
nooseY = None
faceX = None
faceY = None
faceR = None
neckX = None
neckY = None
waistX = None
waistY = None

###########################################################################################
#We need to get another turtle

tWriter = Turtle()
tWriter.color('#692cba')
tWriter.hideturtle()

tBadLetters = Turtle()
tBadLetters.color('#692cba')
tBadLetters.hideturtle()

#variables needed to play game
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
displayWord = ""
secretWord = ""
lettersWrong = ""
lettersCorrect = ""
fails = 7
fontSize = int(sHeight*0.03)
gameDone = False

def displayText(newText):
    tWriter.clear()
    tWriter.penup()
    tWriter.goto(-int(sWidth*0.4), -int(sHeight*0.375))
    tWriter.write(newText, font =('Arial',fontSize, 'bold'))

def displayBadLetters(newText):
    tBadLetters.clear()
    tBadLetters.penup()
    tBadLetters.goto(-int(sWidth*0.4), int(sHeight*0.375))
    tBadLetters.write(newText, font =('Arial',fontSize, 'bold'))

def chooseWord():
    global secretWord
    secretWord = wordBank[randint(0, len(wordBank) - 1)]
    print("The secret word is: " + secretWord)

def makeDisplay():
    global displayWord, secretWord
    displayWord = ""
    for letter in secretWord:
        if letter in alpha:
            if letter.lower() in lettersCorrect.lower():
                displayWord += letter + " "
            else:
                displayWord += "_" + " "
        else:
            displayWord += letter + " "

def getGuess():
    boxTitle = "Letters Used: " + lettersWrong
    guess = s.textinput(boxTitle, "Enter a guess or type $$ to guess the word")
    return guess

def updateHangmanPerson():
    global fails
    if fails == 6:
        drawHead()
    if fails == 5:
        drawBody()
    if fails == 4:
        drawLeftArm()
    if fails == 3:
        drawRightArm()
    if fails == 2:
        drawLeftLeg()
    if fails == 1:
        drawRightLeg()
    if fails == 0:
        drawHappyFace()

def checkWordGuess():
    global gameDone, fails
    boxTitle = "Guess the word!"
    guess = s.textinput(boxTitle, "Enter your guess for the word...")
    if guess.lower() == secretWord.lower():
        displayText("YES!! " + secretWord + " is the word!")
        gameDone = True
    else:
        displayText("No, " + guess + " is not the word.")
        time.sleep(1)
        displayText(displayWord)
        fails -= 1
        updateHangmanPerson()

#this will hold the main loop for the game
def playGame():
    global fails, lettersCorrect, lettersWrong, alpha, gameDone
    while gameDone == False and fails > 0 and "_" in displayWord:

        theGuess = getGuess()

        if theGuess == "$$":
            checkWordGuess()
        elif len(theGuess) > 1 or theGuess == "":
            displayText("No, " + theGuess + " is too many letters")
            time.sleep(1)
            displayText(displayWord)
        elif theGuess not in alpha:
            displayText("No, " + theGuess + " is not a letter")
            time.sleep(1)
            displayText(displayWord)
#we know its a letter now...
        elif theGuess.lower() in secretWord.lower():
# letter is right
            lettersCorrect += theGuess.lower()
            makeDisplay()
            displayText(displayWord)
        elif theGuess not in lettersWrong:
#letter is wrong
            displayText("No!! " + theGuess + " is not in word!")
            time.sleep(1)
            lettersWrong += theGuess.lower() + ", "
            displayBadLetters("Not in word: {" + lettersWrong + "}")
            #lettersWrong += theGuess.lower()
            displayText(displayWord)
            fails -= 1
            updateHangmanPerson()
        else:
        #new will give error
            displayText("No!!!" + theGuess + " is already guesssed")
            time.sleep(1)
            displayText(displayWord)
        if fails <= 0: # if you run out of guesses
            displayBadLetters("No more guesses")
            displayText("You lose. The word was " + secretWord)
            gameDone = True
        if "_" not in displayWord:
            displayBadLetters("You got it!")
            gameDone = True
                      
                        
#makes stars around word
def banner(bannerWord):
    bannerLength = len(bannerWord)

    print("%s" % ("*"*(bannerLength + 4)))
    print("* %s *" % bannerWord)
    print("%s" % ("*"*(bannerLength + 4)))
    


###########################################################################################

def drawGallows():
# Change the variable for every function
    global nooseX, nooseY
    
    t.width(6)
    
    if t.isdown():
        t.penup()

# Setup the starting location of gallow
    gallowX = -int(sWidth*0.25)
    gallowY = -int(sHeight*0.25)
# Gallow width relative to the screen size
    gallowW = int(sWidth*0.5)
# gallow height relative to the screen size
    gallowH = int(sHeight*0.5)

    t.setheading(0)

# goto the gallow beginning
    t.penup()
    t.goto(gallowX, gallowY)

# Start the drawing
    t.pendown()
    t.forward(gallowW)
    t.setpos(gallowW*0.25, gallowY)
    t.left(90)
    t.forward(gallowH)
    t.left(90)
    t.forward(gallowW*0.45)
    t.left(90)
# distance to head
    t.forward(gallowH*.1)
# Save the current location
    nooseX, nooseY = t.position()

def drawHead():
    global faceX
    global faceY
    global faceR
    global neckX
    global neckY

    if t.isdown():
      t.penup()

    hr = int(sWidth*0.09)

    t.goto(nooseX-hr, nooseY-hr)
    t.pendown()
    t.circle(hr)
# save location as middle of the face
    faceX = nooseX
    faceY = nooseY-hr
    faceR = hr
# save location of neck
    neckX = nooseX
    neckY = nooseY-(2*hr)

def drawBody():
    global waistX
    global waistY

    if t.isdown():
        t.penup()

    t.goto(neckX,neckY)
    hr = int(sWidth*0.09)
#set up for body and draw body
    t.pendown()
    t.forward(150)
    t.penup()
    waistX, waistY = t.position()

def drawLeftArm():
#setup for left arm
    if t.isdown():
        t.penup()

    t.goto(neckX,neckY-faceR)
# point the turtle facing the right (East)
    t.setheading(0)
    t.pendown()
#drawing left arm
    t.left(135)
    t.forward(100)

def drawRightArm():
#setup for right arm
    if t.isdown():
        t.penup()

    t.goto(neckX,neckY-faceR)
# point the turtle facing the right (East)
    t.setheading(0)
    t.pendown()
#drawing right arm
    t.left(45)
    t.forward(100)

def drawLeftLeg():
#setup
    if t.isdown():
        t.penup()

    t.goto(waistX,waistY)
# point the turtle facing the right (East)
    t.setheading(0)
    t.pendown()
#drawing
    t.right(135)
    t.forward(100)

    if t.isdown():
        t.penup()

def drawRightLeg():
#setup
    if t.isdown():
        t.penup()

    t.goto(waistX,waistY)
# point the turtle facing the right (East)
    t.setheading(0)
    t.pendown()
#drawing
    t.right(45)
    t.forward(100)

    if t.isdown():
        t.penup()

def drawHappyFace():
    if t.isdown():
      t.penup()

# Draw nose
    t.setheading(0)
    t.goto(faceX,faceY-10)
    sides = 3
    t.pendown()
    for i in range(sides):
      t.fd(10)
      t.left(360/sides)
    t.penup()

# Draw smile
    sr = int(faceR*0.5)
    t.width(3)
    t.setheading(270)
    t.goto(faceX-(faceR/2),faceY-(faceR*.30))
    t.pendown()
    t.circle(sr,180)
    t.penup()

# Draw eyes, right then left
    t.goto(faceX,faceY)
    t.goto(faceX+20, faceY+15)
    t.dot(15)
    t.goto(faceX-20, faceY+15)
    t.dot(15)
    t.penup()

def drawSadFace():
    if t.isdown():
      t.penup()

# Draw nose
    t.setheading(0)
    t.goto(faceX,faceY-10)
    sides = 3
    t.pendown()
    for i in range(sides):
      t.fd(10)
      t.left(360/sides)
    t.penup()

# Draw frown
    sr = int(faceR*0.55)
    t.width(3)
    t.setheading(245)
    t.goto(faceX-(faceR/2),faceY-(faceR*.70))
    t.pendown()
    t.circle(sr,-130)
    t.penup()

# Draw eyes, right then left
    t.goto(faceX,faceY)
    t.goto(faceX+15, faceY+15)
    t.setheading(0)
    t.left(45)
    t.pendown()
    t.forward(18)
    t.backward(9)
    t.left(90)
    t.forward(9)
    t.backward(18)
    t.penup()
    #t.dot(15)
    t.goto(faceX-20, faceY+15)
    t.setheading(0)
    t.left(45)
    t.pendown()
    t.forward(18)
    t.backward(9)
    t.left(90)
    t.forward(9)
    t.backward(18)
    t.penup()
    t.penup()

#Program starts here
drawGallows()
drawHead()
drawBody()
drawLeftArm()
drawRightArm()
drawLeftLeg()
drawRightLeg()
drawHappyFace()
#drawSadFace()

#start playing game
time.sleep(1)
t.clear()
drawGallows()
chooseWord()
makeDisplay()
displayText(displayWord)
displayBadLetters("Not in word: {" + lettersWrong + "}")
playGame()
#banner("Lauren")



