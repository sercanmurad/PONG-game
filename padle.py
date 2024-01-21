from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        # Give the characteristics of the padle
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=4, stretch_len=1)
        # Change position of the padle
        self.penup()
        self.goto(position)

    # Lets move our up and down our paddles with go_up and go_down function
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_dowm(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


