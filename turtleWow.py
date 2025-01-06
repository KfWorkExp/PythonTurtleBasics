import turtle

pen = turtle.Turtle()

def draw_design1():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    initial_size = 150
    
    for i in range(180):
        pen.color(colors[i % 6])
        pen.forward(initial_size)
        pen.right(61)
        pen.forward(initial_size/2)
        pen.right(120)
        pen.forward(initial_size/2)
        pen.right(61)
        pen.forward(initial_size)
        pen.right(181)
    
def draw_design2():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    initial_size = 30  

    for i in range(200):
        pen.color(colors[i % 6])
        pen.forward(initial_size + i)
        pen.left(59)
    
def draw_design3():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    initial_size = 150
    
    for i in range(180):
        pen.color(colors[i % 6])
        pen.forward(initial_size)
        pen.left(59)
        pen.forward(initial_size/2)
        pen.left(91)
        pen.forward(initial_size/2)
        pen.left(59)
        pen.forward(initial_size)
        pen.right(121)
    
    
def draw_design5():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    
    initial_size = 50

    for i in range(300):
        pen.color(colors[i % 6])
        pen.forward(initial_size + i)
        pen.left(150)

def move(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    

wn = turtle.Screen()

wn.setup(width=1000, height=1000)
wn.tracer(0)
wn.bgcolor('black')

mid = 250
mid_neg = -250

pen.hideturtle()
pen.speed(10)
pen.pensize(2)
#pen.bgcolor("black")  

# Call the function to draw the attractive design with black background
move(mid, mid_neg)
draw_design1()

move(mid_neg, mid)
draw_design2()

move(mid, mid)
draw_design3()

move(mid_neg, mid_neg)
draw_design5()

turtle.done()