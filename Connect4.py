import turtle


# The Drawing of the grid with all the empty slots
def draw_grid(grid):
    Pen.setheading(0)
    Pen.goto(-350, 130)
    for rower in range(0, 6):
        for col in range(0, 7):
            if grid[rower][col] == 0:
                Pen.fillcolor("white")
            elif grid[rower][col] == 2:
                Pen.fillcolor("red")
            elif grid[rower][col] == 1:
                Pen.fillcolor("yellow")

            Pen.begin_fill()
            Pen.circle(25)
            Pen.end_fill()

            Pen.penup()
            Pen.forward(58)
            Pen.pendown()
        Pen.setheading(270)
        Pen.penup()
        Pen.forward(58)
        Pen.setheading(180)
        Pen.forward(58 * 7)
        Pen.setheading(0)
        Pen.getscreen().update()


def draw_board():
    Pen.up()
    Pen.setheading(0)
    Pen.goto(-386, -200)
    Pen.begin_fill()
    for b in range(4):
        Pen.color("blue")
        Pen.pendown()
        Pen.forward(420)
        Pen.left(90)
    Pen.up()
    Pen.end_fill()


def draw_game_panel():
    Pen.up()
    Pen.setheading(0)
    Pen.goto(80, 219)
    Pen.begin_fill()
    for rectangle in range(2):
        Pen.color("white")
        Pen.down()
        Pen.forward(250)
        Pen.right(90)
        Pen.forward(418)
        Pen.right(90)
    Pen.end_fill()
    Pen.up()
    Pen.color("black")
    Pen.goto(-150, 250)
    Pen.write("CONNECT 4", True, align="center", font=("Arial", 40, "bold"))


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
    # Diagonal checking
    for d in range(5, 2, -1):
        for c in range(4):
            if grid[d][c] == color and grid[d-1][c+1] == color and grid[d-2][c+2] == color and grid[d-3][c+3] == color:
                return color

    return 0


def display_winner(winners):
    if winners == 2:
        Pen.penup()
        Pen.color("red")
        Pen.goto(200, 150)
        Pen.write("RED WINS", True, align="center", font=("Arial", 20, "bold"))
        Pen.getscreen().update()
        return True
    elif winners == 1:
        Pen.penup()
        Pen.color("yellow")
        Pen.goto(200, 150)
        Pen.write("YELLOW WINS", True, align="center", font=("Arial", 20, "bold"))
        Pen.getscreen().update()
        return True



Pen = turtle.Turtle()
Pen.hideturtle()
Pen.speed(500)
window = turtle.Screen()
window.bgcolor("lightgrey")
Pen.speed(0)
Pen._tracer(8, 25)

# Empty grid initialisation
connect4 = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

draw_game_panel()
draw_board()
draw_grid(connect4)

# Game loop, play up to 42 turns
for player_turn in range(1, 43):
    column_string = window.numinput("Your turn", "Pick column number:", 1, minval=1, maxval=7)
    column = int(column_string)
    column_minus = column - 1
    while connect4[0][column_minus] != 0:
        # This column is already full, pick another one
        column_string = window.numinput("Your turn", "Pick other column number row is full:", 1, minval=1, maxval=7)
        column = int(column_string)
        column_minus = column - 1

    # Make the chips stack up one another
    row = 5
    while connect4[row][column_minus] != 0:
        row = row - 1
    # Find out the colour of the current player (1 or 2)
    playerColor = int((player_turn % 2) + 1)
    # Place the token on the grid
    connect4[row][column_minus] = playerColor
    # Draw the grid
    winner = check_if_winner(connect4, playerColor)
    draw_grid(connect4)
    if display_winner(winner):
        user_input = window.textinput("Exit", "Type 'quit' to exit the game")
        while True:
            if user_input == 'quit':
                print("Game has been exited!")
                break
            else:
                user_input = window.textinput("Exit", "Type 'quit' to exit the game")
        break
    draw_grid(connect4)
