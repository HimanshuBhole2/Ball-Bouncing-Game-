from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(-250,0)
        self.fixed_y = 10
        self.fixed_x = 10
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.fixed_x
        new_y = self.ycor() + self.fixed_y
        self.goto(new_x,new_y)


    def bounce_Y(self):
        self.fixed_y *= -1


    def bounce_X(self):
        self.fixed_x *= -1
        self.move_speed *= 0.9

    def ball_reset(self):
        self.goto(0,0)
        self.fixed_x *= -1