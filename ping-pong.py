import turtle
import time

screen = turtle.Screen()
screen.title("Ping Pong")
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.tracer(0)

# paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = -0.3

# functions
def paddle_1_up():
    y = paddle_1.ycor()
    y = y + 10
    paddle_1.sety(y)
    if y > 240:
        paddle_1.sety(240)

def paddle_1_down():
    y = paddle_1.ycor()
    y = y - 10
    paddle_1.sety(y)
    if y < -240:
        paddle_1.sety(-240)

def paddle_2_up():
    y = paddle_2.ycor()
    y = y + 10
    paddle_2.sety(y)
    if y > 240:
        paddle_2.sety(240)

def paddle_2_down():
    y = paddle_2.ycor()
    y = y - 10
    paddle_2.sety(y)
    if y < -240:
        paddle_2.sety(-240)

screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")




while True:
    screen.update()
    
    # moves the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # ball's borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-290)
        ball.dx *= -1

    time.sleep(0.001)

    # paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
