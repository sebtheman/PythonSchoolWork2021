import turtle as t, time, math
waitTimePerDrawing = 0.2
def clearAndWait(timeToWait):
    time.sleep(timeToWait)
    t.clear()

def drawSquare():
    x = 0
    while x < 4:
        t.forward(100)
        t.right(90)
        x += 1

def drawEquilateralTriangle():
    x = 0
    while x < 3:
        t.left(120)
        t.forward(100)
        x += 1

def drawPentagon():
    x = 0
    while x < 5:
        t.right(72)
        t.forward(100)
        x += 1

def drawHexagon(length):
    x = 0
    while x < 6:
        t.left(60)
        t.forward(length)
        x += 1

def drawPentagram():
    x = 0
    while x < 5:
        t.forward(100)
        t.left(144)
        t.forward(100)
        t.left(72)
        x += 1

def drawNestedSquares(numberOfSquares):
    x = numberOfSquares * 10
    y = 4
    while x != 0:
        while y != 0:
            t.forward(x)
            t.right(90)
            y -= 1
        y = 4
        x -= 10

def drawNestedSquareFunVersion(numberOfSquares, distanceApart, penOffFeatureEnabled):
    x = 4
    while x != 0:
        if penOffFeatureEnabled == False:
            t.penup()
        t.forward(distanceApart)
        t.right(90)
        t.forward(distanceApart)
        t.left(90)
        if penOffFeatureEnabled == False:
            t.pendown()
        drawNestedSquares(numberOfSquares)
        if penOffFeatureEnabled == False:
            t.penup()
        t.backward(distanceApart)
        if penOffFeatureEnabled == False:
            t.pendown()
        t.left(90)
        x -= 1

def drawFan():
    x = 0
    y = 0
    t.right(90)
    while x < 3:
        t.right(30)
        while y < 4:
            t.right(90)
            t.forward(100)
            y += 1
        y = 0
        x += 1

def drawCross(sizeOfCross):
    x = 0
    y = 0
    while x < 4:
        t.left(90)
        t.forward(sizeOfCross)
        while y < 2:
            t.right(90)
            t.forward(sizeOfCross)
            y += 1
        y = 0
        x += 1

def drawSierpinskiTriangle(length):
    lengthOfTriangle = length
    x = 0
    while x < 3:
        t.forward(lengthOfTriangle)
        t.left(120)
        x += 1
    x = 0
    t.left(60)
    lengthOfTriangle /= 2
    t.forward(lengthOfTriangle)
    t.right(60)
    t.forward(lengthOfTriangle)
    while x < 2:
        t.right(120)
        t.forward(lengthOfTriangle)
        x += 1
    x = 0

def fun(angleOne, angleTwo, length, amountOfRepeats):
    for i in range(amountOfRepeats):
        t.left(angleOne)
        t.forward(length)
        t.right(angleTwo)
        t.forward(length)

def drawHoneycomb(length):
    x = [0, 0, 1.5*length, 1.5*length, 0, -1.5*length, -1.5*length]
    y = [0, length*(0.32+math.sqrt(2)), 0.5*length*(0.32+math.sqrt(2)), -0.5*length*(0.32+math.sqrt(2)), -1*length*(0.32+math.sqrt(2)), -0.5*length*(0.32+math.sqrt(2)), 0.5*length*(0.32+math.sqrt(2))]
    for i in range(len(x)):
        t.up()
        t.goto(x[i], y[i])
        t.down()
        drawHexagon(length)

def starting_draw_function():
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.goto(300, 0)
    t.home()
    clearAndWait(waitTimePerDrawing)



def runDrawingProgram(runStart, runSquare, runTriangle, runPentagon, runHexagon, runPentagram, runNestedSquares, runNestedSquaresFunVersion_1, runNestedSquaresFunVersion_2, runFan, runCross, runSierpinskiTriangle, runFun, runHoneycomb):
    t.speed(500)
    if runStart == True:
        starting_draw_function()
    if runSquare == True:
        drawSquare()
        clearAndWait(waitTimePerDrawing)
    if runTriangle == True:
        drawEquilateralTriangle()
        clearAndWait(waitTimePerDrawing)
    if runPentagon == True:
        drawPentagon()
        clearAndWait(waitTimePerDrawing)
    if runHexagon == True:
        drawHexagon(100)
        clearAndWait(waitTimePerDrawing)
    if runPentagram == True:
        drawPentagram()
        clearAndWait(waitTimePerDrawing)
    if runNestedSquares == True:
        drawNestedSquares(20)
        clearAndWait(waitTimePerDrawing)
    if runNestedSquaresFunVersion_1 == True:
        drawNestedSquareFunVersion(20, 30, False)
        clearAndWait(waitTimePerDrawing)
        t.home()
    if runNestedSquaresFunVersion_2 == True:
        drawNestedSquareFunVersion(20, 30, True)
        clearAndWait(waitTimePerDrawing)
        t.home()
    if runFan == True:
        drawFan()
        clearAndWait(waitTimePerDrawing)
    if runCross == True:
        drawCross(150)
        clearAndWait(waitTimePerDrawing)
    if runSierpinskiTriangle == True:
        drawSierpinskiTriangle(200)
        clearAndWait(waitTimePerDrawing)
    if runFun == True:
        fun(161, 53, 50, 100)
        clearAndWait(waitTimePerDrawing)
    if runHoneycomb == True:
        drawHoneycomb(100)
    t.done()

runDrawingProgram(True, True, True, True, True, True, True, True, True, True, True, True, True, True)