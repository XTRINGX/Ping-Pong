# A Simple Pong Game

import turtle
import os

# Set up the screen
wn = turtle.Screen()
wn.title("Pong by King Richard")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = -0.15

# Score variables
score_a = 0
score_b = 0

# Pen to display score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function to move paddle A up
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:  # Boundary checking
        y += 20
    paddle_a.sety(y)

# Function to move paddle A down
def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:  # Boundary checking
        y -= 20
    paddle_a.sety(y)

# Function to move paddle B up
def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:  # Boundary checking
        y += 20
    paddle_b.sety(y)

# Function to move paddle B down
def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:  # Boundary checking
        y -= 20
    paddle_b.sety(y)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.xcor() > 390:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if (ball.dx < 0 and paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50 and ball.xcor() < -340):
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    if (ball.dx > 0 and paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50 and ball.xcor() > 340):
        ball.dx *= -1
        os.system("afplay bounce.wav&")
