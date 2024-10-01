import turtle
import winsound

wn = turtle.Screen()
wn.title('Ping Pong')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_1 = 9
score_2 = 0

# paddle A
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape('square')
paddle_1.color('red')
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# paddle B
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape('square')
paddle_2.color('blue')
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('yellow')
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('yellow')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Jogador 1: {}  Jogador 2: {}'.format(score_1, score_2), align='center', font=('Courier', 24, 'normal'))


# function
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)


# keyboard binding
wn.listen()
wn.onkeypress(paddle_1_up, 'w')
wn.onkeypress(paddle_1_down, 's')
wn.onkeypress(paddle_2_up, 'Up')
wn.onkeypress(paddle_2_down, 'Down')

# window update
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('boing.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('boing.wav', winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write('Jogador 1: {}  Jogador 2: {}'.format(score_1, score_2), align='center', font=('Courier', 24, 'normal'))
        winsound.PlaySound('score.wav', winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write('Jogador 1: {}  Jogador 2: {}'.format(score_1, score_2), align='center', font=('Courier', 24, 'normal'))
        winsound.PlaySound('score.wav', winsound.SND_ASYNC)

    # paddle and ball collisions
    if (340 < ball.xcor() < 350) and (
            paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('boing.wav', winsound.SND_ASYNC)

    if (-340 > ball.xcor() > -350) and (
            paddle_1.ycor() + 40 > ball.ycor() > paddle_1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('boing.wav', winsound.SND_ASYNC)

    if score_1 == 10:
        win_1 = turtle.Turtle()
        win_1.speed(0)
        win_1.color('red')
        win_1.hideturtle()
        win_1.goto(0, 0)
        win_1.write('Jogador 1 venceu!', align='center', font=('Arial', 50, 'normal'))
        paddle_1.hideturtle()
        paddle_2.hideturtle()
        ball.hideturtle()
        ball.goto(0, 0)

    if score_2 == 10:
        win_2 = turtle.Turtle()
        win_2.speed(0)
        win_2.color('blue')
        win_2.hideturtle()
        win_2.goto(0, 0)
        win_2.write('Jogador 2 venceu!', align='center', font=('Arial', 50, 'normal'))
        paddle_1.hideturtle()
        paddle_2.hideturtle()
        ball.hideturtle()
        ball.goto(0, 0)
