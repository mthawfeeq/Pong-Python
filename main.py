from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

ball = Ball()
scoreboard = Scoreboard()
# paddle = Turtle()
# paddle.goto(350, 0)
# paddle.shape("square")
# paddle.penup()
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len=1)

screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.refresh()

    # Detecting Collision with Top and Bottom Wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y_axis()

    # Detecting Collision with the Right Paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x_axis()

    # Detecting Collision with the Left Paddle
    if ball.distance(left_paddle) < 50 and ball.ycor() > -320:
        ball.bounce_x_axis()

    # Detecting Collision with the Right Wall
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detecting Collision with the Left Wall
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
