import turtle

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.speed(10)
my_turtle.pensize(4)
my_turtle.pencolor("purple")

def drawShape():
    for i in range(4):
        my_turtle.forward(100)
        my_turtle.right(90)

drawShape()
turtle.done()

