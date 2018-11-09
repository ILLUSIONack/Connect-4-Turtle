import turtle

YELLOW = 1
RED = 2


# Draw the grid with all the empty slots
def draw_grid(grid):
    myPen.setheading(0)
    myPen.goto(-150, 130)
    for rower in range(0, 6):
        for col in range(0, 7):
            if grid[rower][col] == 0:
                myPen.fillcolor("#FFFFFF")
            elif grid[rower][col] == 2:
                myPen.fillcolor("#FF0000")
            elif grid[rower][col] == 1:
                myPen.fillcolor("#FFFF00")

            myPen.begin_fill()
            myPen.circle(25)
            myPen.end_fill()

            myPen.penup()
            myPen.forward(50)
            myPen.pendown()
        myPen.setheading(270)
        myPen.penup()
        myPen.forward(50)
        myPen.setheading(180)
        myPen.forward(50 * 7)
        myPen.setheading(0)
        myPen.getscreen().update()

def drawsquare():
    myPen.up()
    myPen.setheading(0)
    myPen.goto(-178, -146)
    myPen.begin_fill()
    for b in range(4):
        myPen.color("blue")
        myPen.pendown()
        myPen.forward(355)
        myPen.left(90)
    myPen.up()
    myPen.end_fill()

def check_if_winner(grid, color):
    # Vertical row checking
    for r in range(6):
        for c in range(3):
            if grid[r][c] == color and grid[r][c+1] == color and grid[r][c+2] == color and grid[r][c+3] == color:
                return color
    # Horizontal row checking
    for x in range(3):
        for y in range(7):
            if grid[x][y] == color and grid[x+1][y] == color and grid[x+2][y] == color and grid[x+3][y] == color:
                return color
    # Diagonal checking
    for i in range(3):
        for z in range(3):
            if grid[i][z] == color and grid[i+1][z+1] == color and grid[i+2][z+2] == color and grid[i+3][z+3] == color:
                return color
    return 0


myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(500)
window = turtle.Screen()
window.bgcolor("white")
myPen.speed(0)

# Initialise empty 6 by 7 connect4 grid
connect4 = []
for rows in range(0, 6):
    connect4.append([])
    for cols in range(0, 7):
        connect4[rows].append(0)
drawsquare()
draw_grid(connect4)

# Play the game, take it in turn. Up to 42 turns
for turn in range(1, 43):
    column_string = window.numinput("Your turn", "Pick column number:", 0, minval=1, maxval=7)
    column = int(column_string)
    cadd = column - 1
    while connect4[0][cadd] != 0:
        # This column is already full, pick another one
        column_string = window.numinput("Your turn", "Pick other column number row is full:", 0, minval=1, maxval=7)
        column = int(column_string)
        cadd = column - 1

    # Make the chip slide to the bottom of the board, row starting from 5 then minus 1
    row = 5
    while connect4[row][cadd] != 0:
        row = row - 1
# Find out the colour of the current player (1 or 2)
    playerColor = int((turn % 2) + 1)
    # Place the token on the grid
    connect4[row][cadd] = playerColor
    # Draw the grid

    winner = check_if_winner(connect4, playerColor)
    draw_grid(connect4)
    if winner == 2:
        myPen.penup()
        myPen.color("black")
        myPen.goto(-70, -170)
        myPen.write("RED WINS", True, align="center")
        myPen.getscreen().update()
        break
    elif winner == 1:
        myPen.penup()
        myPen.color("black")
        myPen.goto(-80, -170)
        myPen.write("YELLOW WINS", True, align="center")
        myPen.getscreen().update()
        break
    draw_grid(connect4)
