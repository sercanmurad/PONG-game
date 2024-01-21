from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        #create characteristics of the scoreboard
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        #uptade score method
        self.uptade_score()

    def uptade_score(self):
        #   This method change the score
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align="center",font=("Courier",75,"normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 75, "normal"))

    def left_score(self):
        #change left score
        self.l_score+=1
        self.uptade_score()

    def right_score(self):
        #change right score
        self.r_score+=1
        self.uptade_score()
