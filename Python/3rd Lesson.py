#This is the finished version of the 3rd Lesson
from turtle import Turtle, Screen, speed
import time

global secondaryTitle
secondaryTitle = Turtle()
secondaryTitle.hideturtle()
global title
title = Turtle()
global button2
button2 = Turtle()
global button1
button1 = Turtle()

t = Turtle()
t.hideturtle()

skipStraightToDrawing = False

def drawHouse(
        turtlespeed=3, 
        starting_x=-150, 
        starting_y=-325, 
        stories=2, 
        wallOutlineColor='black', 
        wallFillColor='red', 
        windowOutlineColor='black', 
        doorOutlineColor='black', 
        doorFillColor='brown', 
        doorknobOutlineColor='black', 
        doorknobFillColor='black', 
        roofFillColor='blue', 
        roofOutlineColor='black',
        windows=2
    ):
    t.penup()
    t.goto(starting_x, starting_y)
    t.pendown()
    t.showturtle()
    t.speed(turtlespeed)
    for i in range(stories): #story loop
        t.pensize(5)
        t.pencolor(wallOutlineColor)
        t.fillcolor(wallFillColor)
        t.begin_fill()
        t.penup()
        t.goto(starting_x, starting_y + (200 * i))
        t.pendown()
        for a in range(2): #wall loop
            t.forward(300)
            t.left(90)
            t.forward(200)
            t.left(90)
        t.end_fill()
        for b in range(windows): #window
            t.penup()
            if b <= 1: #Run this for the 1st and 2nd window
                t.goto(starting_x + 10 + (50 * b), starting_y + 90 + (200 * i))
            else: #Run this for the 3rd and 4th video
                t.goto(starting_x + 10 + (50 * b) - 100, starting_y + 90 + (200 * i) + 50) if windows > 3 else t.goto(starting_x + 35 + (50 * b) - 100, starting_y + 90 + (200 * i) + 50)
            t.pendown()
            t.pencolor(windowOutlineColor)
            t.settiltangle(90)
            for c in range(4):
                t.forward(40)
                t.left(90)
            t.forward(20)
            t.left(90)
            t.forward(40)
            t.left(180)
            t.forward(20)
            t.left(90)
            t.forward(20)
            t.left(180)
            t.forward(40)
            t.left(180)
        if i == 0: #Only draw the door if you are on the 1st storey
            t.penup()
            t.goto(starting_x + 210, starting_y)
            t.pendown()
            t.left(90)
            t.pencolor(doorOutlineColor)
            t.fillcolor(doorFillColor)
            t.begin_fill()
            for d in range(2): # door
                t.forward(100)
                t.right(90)
                t.forward(70)
                t.right(90)
            t.end_fill()
            t.speed(500) #Start of doorknob code
            t.penup()
            t.goto(starting_x + 220, starting_y + 60)
            t.pendown()
            t.pencolor(doorknobOutlineColor)
            t.fillcolor(doorknobFillColor)
            t.begin_fill()
            for circleAngle in range(360):
                t.forward(0.05)
                t.right(1)
            t.speed(turtlespeed)
            t.end_fill() #End of doorknob code
            t.right(90)
    t.penup()
    t.setheading(0)
    t.goto(starting_x, starting_y + 200 + (200 * i))
    t.pendown()
    t.pensize(6)
    t.pencolor(roofOutlineColor)
    t.fillcolor(roofFillColor)
    t.begin_fill()
    for b in range(3): #roof loop
        t.forward(300)
        t.left(120)
    t.end_fill()


def handleButton1Click(x, y):
    clearAll()
    drawHouse()

def handleButton2Click(x, y):
    clearAll()
    showTitle('What colour do you want the wall to be?', 'center', ('Arial', 26, 'bold'), 0, 100, 0, 0, 0)
    showSecondaryTitle('Press a number on your keyboard to choose RGB values.', 'center', ('Arial', 18, 'bold'), 0, 75, 0, 0, 0)
    wallColour_red = screen.numinput("Sebastian's House Drawer", "Enter RGB Red value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while wallColour_red == None:
        wallColour_red = screen.numinput("Sebastian's House Drawer", "Enter RGB Red value 0 - 255", default='', minval=0, maxval=255)
        screen.listen()
    wallColour_red = int(wallColour_red)
    wallColour_green = screen.numinput("Sebastian's House Drawer", "Enter RGB Green value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while wallColour_green == None:
        wallColour_green = screen.numinput("Sebastian's House Drawer", "Enter RGB Green value 0 - 255", default='', minval=0, maxval=255)
        screen.listen()
    wallColour_green = int(wallColour_green)
    wallColour_blue = screen.numinput("Sebastian's House Drawer", "Enter RGB Blue value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while wallColour_blue == None:
        wallColour_blue = screen.numinput("Sebastian's House Drawer", "Enter RGB Blue value 0 - 255", default='', minval=0, maxval=255)
        screen.listen()
    wallColour_blue = int(wallColour_blue)
    clearAll()
    showTitle("What colour do you want the wall's outline to be?", 'center', ('Arial', 26, 'bold'), 0, 100, 0, 0, 0)
    showSecondaryTitle('Press a number on your keyboard to choose RGB values.', 'center', ('Arial', 18, 'bold'), 0, 75, 0, 0, 0)
    wallOutlineColour_red = screen.numinput("Sebastian's House Drawer", "Enter RGB Red value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while wallOutlineColour_red == None:
        wallOutlineColour_red = screen.numinput("Sebastian's House Drawer", "Enter RGB Red value 0 - 255", default='', minval=0, maxval=255)
        screen.listen()
    wallOutlineColour_red = int(wallOutlineColour_red)
    wallOutlineColour_green = screen.numinput("Sebastian's House Drawer", "Enter RGB Green value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while wallOutlineColour_green == None:
        wallOutlineColour_green = screen.numinput("Sebastian's House Drawer", "Enter RGB Green value 0 - 255", default='', minval=0, maxval=255)
        screen.listen()
    wallOutlineColour_green = int(wallOutlineColour_green)
    wallOutlineColour_blue = screen.numinput("Sebastian's House Drawer", "Enter RGB Blue value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while wallOutlineColour_blue == None:
        wallOutlineColour_blue = screen.numinput("Sebastian's House Drawer", "Enter RGB Blue value 0 - 255", default='', minval=0, maxval=255)
        screen.listen()
    wallOutlineColour_blue = int(wallOutlineColour_blue)
    clearAll()
    showTitle("What do you want the window's outline colour to be?", 'center', ('Arial', 26, 'bold'), 0, 100, 0, 0, 0)
    showSecondaryTitle("Press a number on your keyboard to choose RGB values", 'center', ('Arial', 18, 'bold'), 0, 75, 0, 0, 0)
    windowOutlineColor_red = screen.numinput("Sebastian's House Drawer", "Enter RGB Red value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while windowOutlineColor_red == None:
        windowOutlineColor_red = screen.numinput("Sebastian's House Drawer", "Enter RGB Red value 0 - 255", minval=0, maxval=255)
        screen.listen()
    windowOutlineColor_red = int(windowOutlineColor_red)
    windowOutlineColor_green = screen.numinput("Sebastian's House Drawer", "Enter RGB Green value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while windowOutlineColor_green == None:
        windowOutlineColor_green = screen.numinput("Sebastian's House Drawer", "Enter RGB Green value 0 - 255", minval=0, maxval=255)
        screen.listen()
    windowOutlineColor_green = int(windowOutlineColor_green)
    windowOutlineColor_blue = screen.numinput("Sebastian's House Drawer", "Enter RGB Blue value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while windowOutlineColor_blue == None:
        windowOutlineColor_blue = screen.numinput("Sebastian's House Drawer", "Enter RGB Blue value 0 - 255", minval=0, maxval=255)
        screen.listen()
    windowOutlineColor_blue = int(windowOutlineColor_blue)
    clearAll()
    showTitle("What do you want the door's outline colour to be?", 'center', ('Arial', 26, 'bold'), 0, 100, 0, 0, 0)
    showSecondaryTitle("Press a number on your keyboard to choose RGB values", 'center', ('Arial', 18, 'bold'), 0, 75, 0, 0, 0)
    doorOutlineColor_red = screen.numinput("Sebastian's House Drawer", "Enter RGB Red value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while doorOutlineColor_red == None:
        doorOutlineColor_red = screen.numinput("Sebastian's House Drawer", "Enter RGB Red value 0 - 255", minval=0, maxval=255)
        screen.listen()
    doorOutlineColor_red = int(doorOutlineColor_red)
    doorOutlineColor_green = screen.numinput("Sebastian's House Drawer", "Enter RGB Green value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while doorOutlineColor_green == None:
        doorOutlineColor_green = screen.numinput("Sebastian's House Drawer", "Enter RGB Green value 0 - 255", minval=0, maxval=255)
        screen.listen()
    doorOutlineColor_green = int(doorOutlineColor_green)
    doorOutlineColor_blue = screen.numinput("Sebastian's House Drawer", "Enter RGB Blue value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while doorOutlineColor_blue == None:
        doorOutlineColor_blue = screen.numinput("Sebastian's House Drawer", "Enter RGB Blue value 0 - 255", minval=0, maxval=255)
        screen.listen()
    doorOutlineColor_blue = int(doorOutlineColor_blue)
    clearAll()
    showTitle("What do you want the door's fill colour to be?", 'center', ('Arial', 26, 'bold'), 0, 100, 0, 0, 0)
    showSecondaryTitle("Press a number on your keyboard to choose RGB values", 'center', ('Arial', 18, 'bold'), 0, 75, 0, 0, 0)
    doorFillColor_red = screen.numinput("Sebastian's House Drawer", "Enter RGB Red value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while doorFillColor_red == None:
        doorFillColor_red = screen.numinput("Sebastian's House Drawer", "Enter RGB Red value 0 - 255", minval=0, maxval=255)
        screen.listen()
    doorFillColor_red = int(doorFillColor_red)
    doorFillColor_green = screen.numinput("Sebastian's House Drawer", "Enter RGB Green value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while doorFillColor_green == None:
        doorFillColor_green = screen.numinput("Sebastian's House Drawer", "Enter RGB Green value 0 - 255", minval=0, maxval=255)
        screen.listen()
    doorFillColor_green = int(doorFillColor_green)
    doorFillColor_blue = screen.numinput("Sebastian's House Drawer", "Enter RGB Blue value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while doorFillColor_blue == None:
        doorFillColor_blue = screen.numinput("Sebastian's House Drawer", "Enter RGB Blue value 0 - 255", minval=0, maxval=255)
        screen.listen()
    doorFillColor_blue = int(doorFillColor_blue)
    clearAll()
    showTitle("What do you want the doorknob's fill colour to be?", 'center', ('Arial', 26, 'bold'), 0, 100, 0, 0, 0)
    showSecondaryTitle("Press a number on your keyboard to choose RGB values", 'center', ('Arial', 18, 'bold'), 0, 75, 0, 0, 0)
    doorknobFillColor_red = screen.numinput("Sebastian's House Drawer", "Enter RGB Red value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while doorknobFillColor_red == None:
        doorknobFillColor_red = screen.numinput("Sebastian's House Drawer", "Enter RGB Red value 0 - 255", minval=0, maxval=255)
        screen.listen()
    doorknobFillColor_red = int(doorknobFillColor_red)
    doorknobFillColor_green = screen.numinput("Sebastian's House Drawer", "Enter RGB Green value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while doorknobFillColor_green == None:
        doorknobFillColor_green = screen.numinput("Sebastian's House Drawer", "Enter RGB Green value 0 - 255", minval=0, maxval=255)
        screen.listen()
    doorknobFillColor_green = int(doorknobFillColor_green)
    doorknobFillColor_blue = screen.numinput("Sebastian's House Drawer", "Enter RGB Blue value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while doorknobFillColor_blue == None:
        doorknobFillColor_blue = screen.numinput("Sebastian's House Drawer", "Enter RGB Blue value 0 - 255", minval=0, maxval=255)
        screen.listen()
    doorknobFillColor_blue = int(doorknobFillColor_blue)
    clearAll()
    showTitle("What do you want the doorknob's outline colour to be?", 'center', ('Arial', 26, 'bold'), 0, 100, 0, 0, 0)
    showSecondaryTitle("Press a number on your keyboard to choose RGB values", 'center', ('Arial', 18, 'bold'), 0, 75, 0, 0, 0)
    doorknobOutlineColor_red = screen.numinput("Sebastian's House Drawer", "Enter RGB Red value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while doorknobOutlineColor_red == None:
        doorknobOutlineColor_red = screen.numinput("Sebastian's House Drawer", "Enter RGB Red value 0 - 255", minval=0, maxval=255)
        screen.listen()
    doorknobOutlineColor_red = int(doorknobOutlineColor_red)
    doorknobOutlineColor_green = screen.numinput("Sebastian's House Drawer", "Enter RGB Green value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while doorknobOutlineColor_green == None:
        doorknobOutlineColor_green = screen.numinput("Sebastian's House Drawer", "Enter RGB Green value 0 - 255", minval=0, maxval=255)
        screen.listen()
    doorknobOutlineColor_green = int(doorknobOutlineColor_green)
    doorknobOutlineColor_blue = screen.numinput("Sebastian's House Drawer", "Enter RGB Blue value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while doorknobOutlineColor_blue == None:
        doorknobOutlineColor_blue = screen.numinput("Sebastian's House Drawer", "Enter RGB Blue value 0 - 255", minval=0, maxval=255)
        screen.listen()
    doorknobOutlineColor_blue = int(doorknobOutlineColor_blue)
    clearAll()
    showTitle("What do you want the roof's fill colour to be?", 'center', ('Arial', 26, 'bold'), 0, 100, 0, 0, 0)
    showSecondaryTitle("Press a number on your keyboard to choose RGB values", 'center', ('Arial', 18, 'bold'), 0, 75, 0, 0, 0)
    roofFillColor_red = screen.numinput("Sebastian's House Drawer", "Enter RGB Red value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while roofFillColor_red == None:
        roofFillColor_red = screen.numinput("Sebastian's House Drawer", "Enter RGB Red value 0 - 255", minval=0, maxval=255)
        screen.listen()
    roofFillColor_red = int(roofFillColor_red)
    roofFillColor_green = screen.numinput("Sebastian's House Drawer", "Enter RGB Green value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while roofFillColor_green == None:
        roofFillColor_green = screen.numinput("Sebastian's House Drawer", "Enter RGB Green value 0 - 255", minval=0, maxval=255)
        screen.listen()
    roofFillColor_green = int(roofFillColor_green)
    roofFillColor_blue = screen.numinput("Sebastian's House Drawer", "Enter RGB Blue value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while roofFillColor_blue == None:
        roofFillColor_blue = screen.numinput("Sebastian's House Drawer", "Enter RGB Blue value 0 - 255", minval=0, maxval=255)
        screen.listen()
    roofFillColor_blue = int(roofFillColor_blue)
    clearAll()
    showTitle("What do you want the roof's outline colour to be?", 'center', ('Arial', 26, 'bold'), 0, 100, 0, 0, 0)
    showSecondaryTitle("Press a number on your keyboard to choose RGB values", 'center', ('Arial', 18, 'bold'), 0, 75, 0, 0, 0)
    roofOutlineColor_red = screen.numinput("Sebastian's House Drawer", "Enter RGB Red value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while roofOutlineColor_red == None:
        roofOutlineColor_red = screen.numinput("Sebastian's House Drawer", "Enter RGB Red value 0 - 255", minval=0, maxval=255)
        screen.listen()
    roofOutlineColor_red = int(roofOutlineColor_red)
    roofOutlineColor_green = screen.numinput("Sebastian's House Drawer", "Enter RGB Green value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while roofOutlineColor_green == None:
        roofOutlineColor_green = screen.numinput("Sebastian's House Drawer", "Enter RGB Green value 0 - 255", minval=0, maxval=255)
        screen.listen()
    roofOutlineColor_green = int(roofOutlineColor_green)
    roofOutlineColor_blue = screen.numinput("Sebastian's House Drawer", "Enter RGB Blue value 0 - 255", minval=0, maxval=255)
    screen.listen()
    while roofOutlineColor_blue == None:
        roofOutlineColor_blue = screen.numinput("Sebastian's House Drawer", "Enter RGB Blue value 0 - 255", minval=0, maxval=255)
        screen.listen()
    roofOutlineColor_blue = int(roofOutlineColor_blue)
    clearAll()
    showTitle("How many stories do you want there to be?", 'center', ('Arial', 26, 'bold'), 0, 100, 0, 0, 0)
    showSecondaryTitle("Minimum Amount: 1. Recommended amount: 1 or 2. Maximum Limit: No limit", 'center', ('Arial', 18, 'bold'), 0, 75, 0, 0, 0)
    numOfStories = screen.numinput("Sebastian's House Drawer", "Enter amount of stories 1 - infinity", minval=1)
    screen.listen()
    while numOfStories == None:
        numOfStories = screen.numinput("Sebastian's House Drawer", "Enter amount of stories 1 - infinity", minval=1)
        screen.listen()
    numOfStories = int(numOfStories)
    clearAll()
    showTitle("What do you want the speed of the turtle to be?", 'center', ('Arial', 26, 'bold'), 0, 100, 0, 0, 0)
    showSecondaryTitle("Minimum Speed: 1. Recommended speed: 3 - 100. Maximum Limit: 500", 'center', ('Arial', 18, 'bold'), 0, 75, 0, 0, 0)
    speedOfTurtle = screen.numinput("Sebastian's House Drawer", "Enter turtle speed 1 - 500", minval=1, maxval=500)
    screen.listen()
    while speedOfTurtle == None:
        speedOfTurtle = screen.numinput("Sebastian's House Drawer", "Enter turtle speed 1 - 500", minval=1, maxval=500)
        screen.listen()
    speedOfTurtle = int(speedOfTurtle)
    clearAll()
    showTitle("What do you want the starting x value to be?", 'center', ('Arial', 26, 'bold'), 0, 100, 0, 0, 0)
    showSecondaryTitle("Minimum value: No limit. Recommended x value: -100 - -300. Maximum Limit: No limit", 'center', ('Arial', 16, 'bold'), 0, 75, 0, 0, 0)
    startingXValue = screen.numinput("Sebastian's House Drawer", "Enter starting X (any number allowed)")
    screen.listen()
    while startingXValue == None:
        startingXValue = screen.numinput("Sebastian's House Drawer", "Enter starting X (any number allowed)")
        screen.listen()
    startingXValue = int(startingXValue)
    clearAll()
    showTitle("What do you want the starting y value to be?", 'center', ('Arial', 26, 'bold'), 0, 100, 0, 0, 0)
    showSecondaryTitle("Minimum value: No limit. Recommended y value: -100 - -300. Maximum Limit: No limit", 'center', ('Arial', 16, 'bold'), 0, 75, 0, 0, 0)
    startingYValue = screen.numinput("Sebastian's House Drawer", "Enter starting Y (any number allowed)")
    screen.listen()
    while startingYValue == None:
        startingYValue = screen.numinput("Sebastian's House Drawer", "Enter starting Y (any number allowed)")
        screen.listen()
    startingYValue = int(startingYValue)
    clearAll()
    showTitle("How many windows do you want there to be?", 'center', ('Arial', 26, 'bold'), 0, 100, 0, 0, 0)
    showSecondaryTitle("Minimum Amount: 1. Recommended amount: 1 - 4. Maximum Limit: 4", 'center', ('Arial', 18, 'bold'), 0, 75, 0, 0, 0)
    numOfWindows = screen.numinput("Sebastian's House Drawer", "Enter amount of windows 1 - 4", minval=1, maxval=4)
    screen.listen()
    while numOfWindows == None:
        numOfWindows = screen.numinput("Sebastian's House Drawer", "Enter amount of windows 1 - 4", minval=1, maxval=4)
        screen.listen()
    numOfWindows = int(numOfWindows)
    clearAll()
    showTitle("All values have been entered", 'center', ('Arial', 26, 'bold'), 0, 100, 0, 0, 0)
    time.sleep(0.5)
    clearAll()
    showTitle("Drawing house in...", 'center', ('Arial', 26, 'bold'), 0, 100, 0, 0, 0)
    for timer in range(3, 0, -1):
        time.sleep(1)
        secondaryTitle.clear()
        showSecondaryTitle(timer, 'center', ('Arial', 20, 'bold'), 0, 75, 0, 0, 0)
    time.sleep(1)
    clearAll()
    drawHouse(
        turtlespeed=speedOfTurtle, 
        starting_x=startingXValue, 
        starting_y=startingYValue, 
        stories=numOfStories, 
        wallOutlineColor=(wallOutlineColour_red, wallOutlineColour_green, wallOutlineColour_blue), 
        wallFillColor=(wallColour_red, wallColour_green, wallColour_blue), 
        windowOutlineColor=(windowOutlineColor_red, windowOutlineColor_green, windowOutlineColor_blue), 
        doorOutlineColor=(doorOutlineColor_red, doorOutlineColor_green, doorOutlineColor_blue), 
        doorFillColor=(doorFillColor_red, doorFillColor_green, doorFillColor_blue), 
        doorknobOutlineColor=(doorknobOutlineColor_red, doorknobOutlineColor_green, doorknobOutlineColor_blue), 
        doorknobFillColor=(doorknobFillColor_red, doorknobFillColor_green, doorknobFillColor_blue), 
        roofFillColor=(roofFillColor_red, roofFillColor_green, roofFillColor_blue), 
        roofOutlineColor=(roofOutlineColor_red, roofOutlineColor_green, roofOutlineColor_blue),
        windows=numOfWindows
    )

def clearAll():
    button1.clear()
    button1.hideturtle()
    button2.clear()
    button2.hideturtle()
    title.clear()
    secondaryTitle.clear()

def showButton1():
    button1.speed(500)
    button1.penup()
    button1.goto(-200, 30)
    button1.write('Default settings', align='center', font=('Arial', 24, 'bold'))
    button1.goto(-175, 0)
    button1.fillcolor('green')
    button1.turtlesize(3,5,1)
    button1.onclick(handleButton1Click)
    button1.showturtle()

def showButton2():
    button2.speed(500)
    button2.penup()
    button2.goto(200, 30)
    button2.write('Make your own settings', align='center', font=('Arial', 24, 'bold'))
    button2.goto(173, 0)
    button2.fillcolor('red')
    button2.left(180)
    button2.turtlesize(3,5,1)
    button2.onclick(handleButton2Click)
    button2.showturtle()

def showTitle(message, alignment, font, x, y, r, g, b):
    screen = Screen()
    title.hideturtle()
    title.speed(500)
    title.penup()
    title.goto(x, y)
    screen.colormode(255)
    title.pencolor(r, g, b)
    title.write(message, align=alignment, font=font)

def showSecondaryTitle(message, alignment, font, x, y, r, g, b):
    screen = Screen()
    secondaryTitle.hideturtle()
    secondaryTitle.speed(500)
    secondaryTitle.penup()
    secondaryTitle.goto(x, y)
    screen.colormode(255)
    secondaryTitle.pencolor(r, g, b)
    secondaryTitle.write(message, align=alignment, font=font)


if skipStraightToDrawing == False:
    showButton1()
    showButton2()
    showTitle('Do you want to use default settings or make your own settings?', 'center', ('Arial', 20, 'bold'), 0, 100, 0, 0, 0)
else:
    button1.hideturtle()
    button2.hideturtle()
    title.hideturtle()
    drawHouse()

screen = Screen()
screen.mainloop()