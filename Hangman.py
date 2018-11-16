from turtle import *

wordBank = ['awkward', 'absurd', 'avenue', 'abyss', 'bagpipes', 'banjo', 'beekeeper', \
            'bikini', 'blizzard', 'boggle', 'bookworm', 'boxcar', 'buckaroo', 'bungler', \
            'cobweb', 'crypt', 'cycle', 'dizzying', 'dwarves', 'embezzle', 'fishhook', \
            'gazebo', 'gypsy', 'haiku', 'haphazard', 'ivory', 'jazzy', 'jukebox', \
            'kayak', 'kiosk', 'memento', 'mystify', 'oxygen', 'pajamas', 'pixel', \
            'rhythmic', 'rogue', 'swivel', 'unzip', 'waxy', 'wildebeest', 'yacht' \
            'zigzag', 'zombie']

sWidth = 600
sHeight = 800
s = getscreen()
s.setup(sWidth, sHeight)
s.bgcolor('#aafff8')

t=getturtle()
t.color('#8d71fc')
t.width(6)

def drawGallows():
    t.penup()
    t.goto(-int(sWidth*0.25), -int(sHeight*0.25))
    t.pendown()
    t.forward(int(sWidth*0.5))

    t.left(180)
    t.forward(60)
    t.right(90)
    t.forward(420)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(50)

def drawHead():
    hr = int(sWidth*0.09)
    t.penup()
    t.goto(t.xcor()-hr, t.ycor()- hr)
    t.pendown()
    t.circle(hr)

def drawBody():
    hr = int(sWidth*0.09)
#set up for body
    t.penup()
    t.goto(t.xcor()+hr, t.ycor()-hr)
#drawing body
    t.pendown()
    t.forward(150)

def drawLeftArm():
#setup for left arm
    t.penup()
    t.left(180)
    t.forward(90)
    t.pendown()
#drawing left arm
    t.left(50)
    t.forward(100)

def drawRightArm():
#setup for right arm
    t.penup()
    t.backward(100)
    t.pendown()
#drawing right arm
    t.right(100)
    t.forward(100)

def drawLeftLeg():
#setup
    t.penup()
    t.backward(100)
    t.right(130)
    t.pendown()
#drawing
    t.forward(100)
    t.left(30)
    t.forward(100)

def drawRightLeg():
#setup
    t.penup()
    t.backward(100)
    t.pendown()
#drawing
    t.right(60)
    t.forward(100)


    
   
#Program starts here
drawGallows()
drawHead()
drawBody()
drawLeftArm()
drawRightArm()
drawLeftLeg()
drawRightLeg()
