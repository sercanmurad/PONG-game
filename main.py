from turtle import Screen
from padle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
#Creat the game screen and his parameters
screen=Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("Pong Game")
#use tracer function to do not see the padle when it moves to the x and y cordinant from center
screen.tracer(0)
#Create the two padles with using a padle class
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
#Create the scoreboard
score=Scoreboard()
#Create a ball using ball clas
ball=Ball()
#Listen the user to move padle
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_dowm, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_dowm, "s")

#Create a while loop for the game
game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    #Detect collusion with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()

    #Detect collusion with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect  R paddle is mising
    if ball.xcor() > 380:
        ball.reset_position_r()
        score.left_score()
    #Detect L paddle is mising
    if ball.xcor() < -380:
        ball.reset_position_l()
        score.right_score()


#Close the screen when we click
screen.exitonclick()