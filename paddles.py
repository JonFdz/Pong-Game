from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.setheading(UP)
        self.resizemode("user")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.color("white")
        self.setposition(position)

    def move_up(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.setheading(DOWN)
        self.forward(MOVE_DISTANCE)