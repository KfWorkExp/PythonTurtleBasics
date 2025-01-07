# Python Basics with Turtle

## Introduction

Each of the files in this Repo give examples of Python code 
The aim is to get students coding in Python using the turtle package before they move onto the more advanced TicTacToe exercise.

## Initial setup

### Step 1 - The following software needs to be installed on your laptop:

- [Visual Studio Code](https://code.visualstudio.com/) - Code Editor/Compiler
- [Python](https://www.python.org/downloads/) - compiler and runner for Python code.
- [Git](https://git-scm.com/) - Scource code management.

### Step 2 - Fork the Master Repo and create a working copy on your laptop.

1) First on your local machine, create a directory where you are going to work (e.g. c:\code).
2) Go to [GitHub](https://github.com/) and create yourself an account (don't forget to verify your email address).
3) Go to our seed repository and create a copy in your own account by clicking the 'fork' button.
4) In your new repo  click the green 'Code' button, and copy the url on the https tab.
5) In windows open a command prompt, 
      a) Create a 'code' folder: mkdir code
      b) Navigate to it: cd code
      c) Copy the code to your laptop: git clone <url>  (where the url is the one you copied in 4).

Note that 'forking' only copies the code and not the Wiki with the user stories etc in.  You will need to refer to the original url for these.

### Step 3 - Open in VS Code and run up the code.

1) Open VS Code.
2) Goto File -> Open Folder and select the top level folder that was exported from Git.
3) This opens up the source code in VS Code.
4) Next go to Terminal -> New Terminal.
5) In the terminal window type 'cd <path>' where path is the path to the top level folder you just opened (you can copy it from Windows Explorer)
6) Type: 'python <file name>' and press return.

### Step 4 - Push your changes into your repository

1) Open a new terminal by going to Terminal -> New Terminal.
2) Check that you have your git credentials set
   `git config --list` is the command
3) Set up your username and email if it is missing from the git config list
   `git config --global user.name "Your Name"`
   `git config --global user.email "your.email@email.com"`
4) Commit your local changes on your machine
   `git add .` Adds all local changes for committing
   `git commit -m"enter message here"` Commits the changes so they can be pushed under a message you set
5) Push your changes to your GitHub remote repository
   `git push origin HEAD` 

## Challenges

1) Take the code in TurtleBasic.py and turn it into something prettier?
        - Try changing  the start point and turn before drawing each time
        - Experiment with pen colours and fill.  What cool effects can you create?
   
     
2) Can you figure out how to draw some other basic shapes?
        - Triangle (3 sides, internal angles 60 degrees)
        - Pentagon (5 sides, internal angles 108 degrees)
        - Hexagon (6 sides, internal angles 120 degrees)
        - Octagon (8 sides, internal angles 135 degrees)
   
 
3) Try making some more complex drawings for example:
        - A house, spiders web, tree or animal
        - Draw letters to spell your name or a simple word
        - Create a 3-dimensional object such as a cube or a pyramid.


4) Can you make the code from 3 generic so that the user inputs a number of sides and it calculates how to draw the required shape?
  

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

## Python Help

- [https://www.w3schools.com/python/](https://www.w3schools.com/python/)
- [https://www.w3schools.com/python/python_user_input.asp](https://www.w3schools.com/python/python_user_input.asp)
- [https://www.geeksforgeeks.org/python-turtle-tutorial/] (https://www.geeksforgeeks.org/python-turtle-tutorial/)
