from turtle import Turtle, Screen
from random import randint
from scores import storescore, high_score

# basic config
win = Screen()

win.title("Turtle Game") # title of pop up window
t = Turtle("turtle")
win.setup(500, 500)
win.bgpic("gamebg.png")

t.penup()

# turtle outline
t.pencolor('white')
t.pensize(5)

# Define the movement functions
def move_up():
    t.setheading(90)
    t.forward(10)

def move_down():
    t.setheading(270)
    t.forward(10)

def move_left():
    t.setheading(180)
    t.forward(10)

def move_right():
    t.setheading(0)
    t.forward(10)

def game_over(): # function that runs when game ends
    t.hideturtle()
    t.penup()
    t.goto(0, 0)
    t.write("Game Over", align="center", font=("Arial", 24, "normal"))
    t.goto(0, -50)
    t.write(f"Score: {(t.shapesize()[0])}", align="center", font=("Arial", 18, "normal"))
    storescore((t.shapesize()[0]))
    
# Define the movement function
def move_forward():
    t.forward(10)

    # Check if the turtle eats an apple
    for apple in apples:
        if t.distance(apple) < 20:
            t.shapesize(t.shapesize()[0]+1, t.shapesize()[1]+1) # increase turtle size
            apple.hideturtle() # hide apple
            apples.remove(apple) # remove apple from list
            spawn_apple() # spawn a new apple

    # Check if the turtle is out of bounds
    x, y = t.position()
    if abs(x) > win.window_width() / 2 or abs(y) > win.window_height() / 2:
        game_over() # call the game over function with the turtle's size as the score
        return

    if not paused:
        win.ontimer(move_forward, 100) # schedule the function to be called again after 100 milliseconds

# Function to spawn a new apple
def spawn_apple():
    apple = Turtle(shape="circle")
    apple.color("red")
    apple.penup()
    apple.goto(randint(-200, 200), randint(-200, 200))
    apples.append(apple)

# Create the first apple
apples = []
spawn_apple()

# Bind the movement functions to the keyboard keys
win.onkeypress(move_up, 'Up')
win.onkeypress(move_down, 'Down')
win.onkeypress(move_left, 'Left')
win.onkeypress(move_right, 'Right')
win.listen()

paused = False

# Define the pause_game function
def pause_game():
    print("||")
    global paused
    if not paused:
        paused = True
    else:
        paused = False
        move_forward()

win.onkeypress(pause_game, 'space') # bind the pause_game function to the spacebar key

def display(highscore):
  t.penup()
  t.goto(-win.window_width() // 2 + 20, win.window_height() // 2 - 40)  # Move turtle to top left of screen
  t.write(f"High Score: {high_score()}", align="left", font=("Arial", 10, "bold"))

display(high_score())

move_forward()

win.mainloop()
