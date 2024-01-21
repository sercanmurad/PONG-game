
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        #Create a parameters of the ball
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.penup()
        self.x_move=10
        self.y_move=10
        self.move_speed=0.1
    def move(self):
        #move the ball with using a x and y move methods with 10
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)
    def bounce_y(self):
        #when the ball hit the wall we reverse the y_move
        self.y_move *=-1
    def bounce_x(self):
        #when the ball collusion to the paddles we reverse his x move cordinates
        self.x_move *=-1
        self.move_speed *=0.9
    def reset_position_r(self):
        #reset  position when right paddle miss
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_x()

    def reset_position_l(self):
        #reset position when the left position miss
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_x()

