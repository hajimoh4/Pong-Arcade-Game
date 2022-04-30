from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong Arcade game")
screen.tracer(0)

l_paddle = (-350, 0)
r_paddle = (350, 0)

left_paddle = Paddle(l_paddle)
right_paddle = Paddle(r_paddle)
ball = Ball()
score = Scoreboard()










screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_on = True

while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    ## Detect collission with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ##Needs to bounce
        ball.bounce_y()

    ##Detect collission with right paddle
    elif ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    elif ball.xcor() > 400:
        score.left_score +=1
        ball.reset_position() 
        score.update_score()
        time.sleep(1.5)
        
    elif ball.xcor() < -400:
        score.right_score += 1
        ball.reset_position()
        score.update_score()
        time.sleep(1.5)



screen.exitonclick()