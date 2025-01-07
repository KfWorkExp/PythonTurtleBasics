# Python Basics with Turtle

## Introduction

Each of the files in this Repo give examples of Python code 

## Challenges

1) Take the code in TurtleBasic.py and turn it into something prettier?
   - Try changing  the start point and turn before drawing each time
   - Experiment with pen colours and fill.  What cool effects can you create?
     
3) Can you figure out how to draw some other basic shapes?
     - Triangle (3 sides, internal angles 60 degrees)
     - Pentagon (5 sides, internal angles 108 degrees)
     - Hexagon (6 sides, internal angles 120 degrees)
     - Octagon (8 sides, internal angles 135 degrees)
 
4) Try making some more complex drawings for example:
  - A house, a tree or an animal
  - Draw letters to spell your name or a simple word
  - Create a 3-dimensional object such as a cube or a pyramid.

5) Can you make the code from 3 generic so that the user inputs a number of sides and it calculates how to draw the required shape?

## Turtle Commands

| METHOD | PARAMETER | DESCRIPTION |
| :------- | :------------: | :---------------------------------------- |
| Turtle() | None | 	It creates and returns a new turtle object |
| forward() | amount | It moves the turtle forward by the specified amount |
| backward() | amount | It moves the turtle backward by the specified amount |
| right() | angle | It turns the turtle clockwise |
| left() | angle | It turns the turtle counter clockwise |
| penup() | None | It picks up the turtle’s Pen |
| pendown() | None | Puts down the turtle’s Pen |
| up() | None | Picks up the turtle’s Pen |
| down() | None | Puts down the turtle’s Pen |
| color() | Color name | Changes the color of the turtle’s pen |
| fillcolor() |	Color name | Changes the color of the turtle will use to fill a polygon |
| heading() | None | It returns the current heading |
| position() | None | It returns the current position |
| goto() | x, y | It moves the turtle to position x,y |
| begin_fill() | None | Remember the starting point for a filled polygon |
| end_fill() | None | It closes the polygon and fills with the current fill colour |
| dot() | None | Leaves the dot at the current position |
| stamp() | None | Leaves an impression of a turtle shape at the current location |
| shape() | shapename | Should be ‘arrow’, ‘classic’, ‘turtle’ or ‘circle’ |

## Running Python Code in VS Code

How to run your code
1)	Select ‘terminal -> new terminal from the menu bar.
2)	In the new terminal window change to the folder where your file is 
    cd <path>
    TIP: Copy the path from windows explorer.	
3)	Run the code type:
    python <file name> 
