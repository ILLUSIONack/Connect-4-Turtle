import turtle

# Draw the grid with all the empty slots
def draw_grid(grid):
    myPen.setheading(0)
    myPen.goto(-350, 130)
    for rower in range(0, 6):
        for col in range(0, 7):
            if grid[rower][col] == 0:
                myPen.fillcolor("white")
            elif grid[rower][col] == 2:
                myPen.fillcolor("red")
            elif grid[rower][col] == 1:
                myPen.fillcolor("yellow")

            myPen.begin_fill()
            myPen.circle(25)
            myPen.end_fill()

            myPen.penup()
            myPen.forward(58)
            myPen.pendown()
        myPen.setheading(270)
        myPen.penup()
        myPen.forward(58)
        myPen.setheading(180)
        myPen.forward(58 * 7)
        myPen.setheading(0)
        myPen.getscreen().update()


def draw_board():
    myPen.up()
    myPen.setheading(0)
    myPen.goto(-386, -200)
    myPen.begin_fill()
    for b in range(4):
        myPen.color("blue")
        myPen.pendown()
        myPen.forward(420)
        myPen.left(90)
    myPen.up()
    myPen.end_fill()


def draw_gamepanel():
    myPen.up()
    myPen.setheading(0)
    myPen.goto(80, 219)
    myPen.begin_fill()
    for rectangle in range(2):
        myPen.color("white")
        myPen.down()
        myPen.forward(250)
        myPen.right(90)
        myPen.forward(418)
        myPen.right(90)
    myPen.end_fill()
    myPen.up()
    myPen.color("black")
    myPen.goto(-150, 250)
    myPen.write("CONNECT 4", True, align="center", font=("Arial", 40, "bold"))


def check_if_winner(grid, color):
    # Vertical row checking
    for r in range(6):
        for c in range(4):
            if grid[r][c] == color and grid[r][c+1] == color and grid[r][c+2] == color and grid[r][c+3] == color:
                return color
    # Horizontal row checking
    for x in range(3):
        for y in range(7):
            if grid[x][y] == color and grid[x+1][y] == color and grid[x+2][y] == color and grid[x+3][y] == color:
                return color
    # Diagonal checking
    for i in range(3):
        for z in range(4):
            if grid[i][z] == color and grid[i+1][z+1] == color and grid[i+2][z+2] == color and grid[i+3][z+3] == color:
                return color
    #diagonal checking
    for d in range(5,2,-1):
        for c in range(4):
            if grid[d][c] == color and grid[d-1][c+1] == color and grid[d-2][c+2] == color and grid[d-3][c+3] == color:
                return color

    return 0


myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(500)
window = turtle.Screen()
window.bgcolor("lightgrey")
myPen.speed(0)
myPen._tracer(8, 25)

# Initialise empty 6 by 7 connect4 grid
connect4 = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

draw_gamepanel()
draw_board()
draw_grid(connect4)

# Play the game, take it in turn. Up to 42 turns
for turn in range(1, 43):
    column_string = window.numinput("Your turn", "Pick column number:", 1, minval=1, maxval=7)
    column = int(column_string)
    column_minus = column - 1
    while connect4[0][column_minus] != 0:
        # This column is already full, pick another one
        column_string = window.numinput("Your turn", "Pick other column number row is full:", 1, minval=1, maxval=7)
        column = int(column_string)
        column_minus = column - 1

    # Make the chip slide to the bottom of the board, row starting from 5 then minus 1
    row = 5
    while connect4[row][column_minus] != 0:
        row = row - 1
    # Find out the colour of the current player (1 or 2)
    playerColor = int((turn % 2) + 1)
    # Place the token on the grid
    connect4[row][column_minus] = playerColor
    # Draw the grid

    winner = check_if_winner(connect4, playerColor)
    draw_grid(connect4)
    if winner == 2:
        myPen.penup()
        myPen.color("red")
        myPen.goto(200, 150)
        myPen.write("RED WINS", True, align="center", font=("Arial", 20, "bold"))
        myPen.getscreen().update()
        user_input = window.textinput("Exit", "Type 'quit' to exit the game")
        game_over = True
        while game_over:
            if user_input == 'quit':
                game_over = False
                print("Game has been exited!")
            else:
                user_input = window.textinput("Exit", "Type 'quit' to exit the game")
        break
    elif winner == 1:
        myPen.penup()
        myPen.color("Yellow")
        myPen.goto(200, 150)
        myPen.write("YELLOW WINS", True, align="center", font=("Arial", 20, "bold"))
        myPen.getscreen().update()
        user_input = window.textinput("Exit", "Type 'quit' to exit the game")
        game_over = True
        while game_over:
            if user_input == 'quit':
                game_over = False
                print("Game has been exited!")
            else:
                user_input = window.textinput("Exit", "Type 'quit' to exit the game")
        break
    draw_grid(connect4)
