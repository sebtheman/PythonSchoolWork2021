from turtle import Turtle, Screen

t = Turtle()

t.hideturtle()

def petal(color, size, speed):
    t.speed(speed)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(size, 70)
    t.left(110)
    t.circle(size, 70)
    t.end_fill()

    
def drawPetals(colorOne, colorTwo, size=300, speed=100):
    for repeats in range(9):
        petal(colorOne, size, speed) if repeats % 2 == 0 else petal(colorTwo, size, speed)
        t.setheading(45 * repeats)


def start():
    t.speed(100)
    t.setheading(270)
    t.pensize(20)
    t.forward(350)
    t.backward(350)
    t.pensize(1)
    drawPetals('red', 'yellow')
    drawPetals('yellow', 'red', size=100)
    t.goto(0, -50)
    t.fillcolor('black')
    t.begin_fill()
    t.circle(50)
    t.end_fill()


start()

screen = Screen()
screen.mainloop()

