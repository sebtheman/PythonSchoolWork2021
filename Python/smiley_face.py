######################################################################################################################
#                                                                                                                    #
#                                                                                                                    #
#                                                                                                                    #
# Code is fully scalable and customizable                                                                            #
# You can go into the function and change any value, including the size, and the drawing will still work as intended #
# TODO: Add the ability to change settings using Turtle instead of having to go into the code and change it manually #
#                                                                                                                    #
#                                                                                                                    #
######################################################################################################################
import random
import turtle as t

def goTo(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_face(
            speed=100,
            size=60,
            fillColor='yellow',
            penColor='black',
            eyeOutlineColor='black',
            eyeFillColor='white',
            pupilOutlineColor='black',
            pupilFillColor='black',
            noseOutlineColor='black',
            noseFillColor='black',
            smileOutlineColor='black',
            tongueOutlineColor='black',
            tongueFillColor='red',
            timesToRepeat=10,
            x_max = 300,
            x_min = -300,
            y_max = 300,
            y_min = -300
        ):
    t.showturtle()
    t.speed(speed)
    for i in range(timesToRepeat):
        x = random.randint(x_min, x_max)
        y = random.randint(y_min, y_max)
        goTo(x, y)
        t.pencolor(penColor)
        t.fillcolor(fillColor)
        t.begin_fill()
        t.circle(size)
        t.end_fill()
        for a in range(2): #Eyes
            goTo(x - size / 2.3, y + (size * 1.2)) if a == 0 else goTo(x + size / 2.3, y + (size * 1.2))
            t.pencolor(eyeOutlineColor)
            t.fillcolor(eyeFillColor)
            t.begin_fill()
            t.circle(size / 4)
            t.end_fill()
            # From here below is for pupils
            goTo(x - size / 2.4, y + (size * 1.28)) if a == 0 else goTo(x + size / 2.4, y + (size * 1.28))
            t.pencolor(pupilOutlineColor)
            t.fillcolor(pupilFillColor)
            t.begin_fill()
            t.circle(size / 8)
            t.end_fill()
            # End of pupil code
        # Nose code
        goTo(x + size * 0.015, y + size * 0.9)
        t.pencolor(noseOutlineColor)
        t.fillcolor(noseFillColor)
        t.begin_fill()
        t.circle(size / 9)
        t.end_fill()
        # End of nose code
        # Tongue code
        goTo(x - size * 0.08, y + (size * 0.4101))
        t.pencolor(tongueOutlineColor)
        t.fillcolor(tongueFillColor)
        t.right(90)
        t.begin_fill()
        t.circle(size / 9, 180)
        t.end_fill()
        t.left(180)
        # End of tongue code
        # Smile code
        goTo(x - size * 0.375, y + (size * 0.8))
        t.pencolor(smileOutlineColor)
        t.circle(size / 2.5, 180)
        t.left(270)
        # End of smile code
    t.done()


draw_face()
