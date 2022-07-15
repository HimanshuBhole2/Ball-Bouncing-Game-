from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        y_new1 = self.ycor() + 20
        self.goto(self.xcor(), y = y_new1)

    def downward(self):
        y_new2 = self.ycor() - 20
        self.goto(self.xcor(), y = y_new2)
