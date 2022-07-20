import turtle

# screen setup
wn = turtle.Screen()
wn.title("pong by Bala")
wn.bgcolor("black")
wn.setup(width=800, height=600)

# pad A
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("white")
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.penup()
pad_a.goto(-350, 0)

# pad B
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.penup()
pad_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(10)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2


# paddle_move
def pad_a_up():
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)


def pad_a_down():
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)


def pad_b_up():
    y = pad_b.ycor()
    y += 20
    pad_b.sety(y)


def pad_b_down():
    y = pad_b.ycor()
    y -= 20
    pad_b.sety(y)


# keyboard listening
wn.listen()
wn.onkeypress(pad_a_up, "w")
wn.onkeypress(pad_a_down, "s")
wn.onkeypress(pad_b_up, "Up")
wn.onkeypress(pad_b_down, "Down")

while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # check border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1

    if (330 < ball.xcor() < 350) and (pad_b.ycor() + 40 > ball.ycor() > pad_b.ycor() - 40):
        ball.dx *= -1

    if (-330 > ball.xcor() > -350) and (pad_a.ycor() + 40 > ball.ycor() > pad_a.ycor() - 40):
        ball.dx *= -1

