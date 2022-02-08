###############################################################################################################################################
#                                                                                                                                             #
#                                                                                                                                             #
# THIS IS AN OLD FILE WITH VERY BAD CODE AND THIS IS VERY FEATURE UNCOMPLETE. PLEASE GO TO 3rd Lesson.py TO SEE WHAT I DID FOR THE 3RD LESSON.#
# I STOPPED WORKING ON THIS FILE AND REWROTE ALL OF THE CODE IN 3rd Lesson.py SO THIS CODE IS VERY BROKEN                                     #
#                                                                                                                                             #
#                                                                                                                                             #
###############################################################################################################################################
import turtle as t

def drawHouse(
    startX, 
    startY,
    stories,
    wallOutlineSize,
    turtleSpeed,
    wallColor,
    wallX,
    wallY,
    wallOutlineColor,
    windows,
    windowOutlineColor,
    windowGlassColor,
    doorColor,
    doorX,
    doorY,
    windowX,
    windowY,
    doorOutlineColor,
    doorknobColor,
    doorknobOutlineColor,
    doorknobX,
    doorknobY,
    roofColor,
    roofX,
    roofY,
    roofOutlineColor,
    roofShape,
    windowOutlineSize,
    doorOutlineSize,
    doorknobOutlineSize,
    roofOutlineSize,
    doorMarginX,
    doorMarginY,
    windowMarginY,
    windowMarginX,
    doorknobMarginX,
    doorknobMarginY,):
    t.penup()
    t.goto(startX, startY)
    t.pendown()
    t.speed(turtleSpeed)
    for i in range(stories):
        if i > 0:
            t.penup()
            t.goto(startX, startY*(wallY*i))
        t.pensize(wallOutlineSize)
        t.pencolor(wallOutlineColor)
        t.fillcolor(wallColor)
        t.begin_fill()
        for a in range(4):
            t.forward(wallX)
            t.left(90)
            t.forward(wallY)
        t.end_fill()


initialInput = input("Do you want to use default values, use your own values, or end the program? (Press Y + Enter for default values, press N + Enter to choose your own values, and type End to end the program)")   
if initialInput == 'Y':
    drawHouse(0, 0, 2, 5, 1, 'brown', 300, 100, 'black', 2, 'black', 'white', 'brown', 30, 100, 10, 10, 'black', 'yellow', 'black', 5, 5, 'pink', 200, 200, 'black', 'triangle', 3, 5, 1, 5, 170, 0, 120, 20, 20, 80)
    t.done()
elif initialInput == "N":
    print("Coming soon")
    t.done()
elif initialInput == "End":
    quit()
else: 
    print("Wrong answer. Please try again but submit Y or N. Y for default values and N to make your own values")
    while initialInput != 'N' or initialInput != 'Y' or initialInput != "End":
        initialInput = input("Do you want to use default values, use your own values, or end the program? (Press Y + Enter for default values, press N + Enter to choose your own values, and type End to end the program)")
        if initialInput == 'Y':
            drawHouse(0, 0, 1, 5, 500, 'brown', 200, 200, 'black', 2, 'black', 'white', 'brown', 30, 100, 10, 10, 'black', 'yellow', 'black', 5, 5, 'pink', 200, 200, 'black', 'triangle', 3, 5, 1, 5, 170, 0, 120, 20, 20, 80)
            t.done()
        elif initialInput == "N":
            print("Coming soon")
            t.done()
        elif initialInput == "End":
            quit()
        else:
            print("Wrong answer. Please try again but submit Y, N, or End. Y for default values, N to make your own values, and End to end the program")