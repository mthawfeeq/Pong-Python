from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        new_y_coordinate = self.ycor() + 20
        self.goto(self.xcor(), new_y_coordinate)

    def down(self):
        new_y_coordinate = self.ycor() - 20
        self.goto(self.xcor(), new_y_coordinate)

