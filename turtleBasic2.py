import turtle

my_turtle = turtle.Turtle()


def drawShape(sideSize):
    for i in range(4):
        my_turtle.forward(sideSize)
        my_turtle.right(90)
        
def drawFlower(numTurns, turnsize, sideSize, lineColour, fillColour):
    
    my_turtle.begin_fill()
    my_turtle.fillcolor(fillColour)
    my_turtle.pencolor(lineColour)
    
    for i in range(numTurns):
        drawShape(sideSize)
        my_turtle.right(turnsize)
        #my_turtle.forward(20)
        
    my_turtle.end_fill()
        

def main():  
    my_turtle.shape("turtle")
    my_turtle.speed(10)
    my_turtle.pensize(4)
        
    drawFlower(10, 36, 300, "red", "purple")
    my_turtle.right(10)
    drawFlower(10, 36, 100, "yellow", "pink")

main()    
turtle.done()

