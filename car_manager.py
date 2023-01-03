from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
POSITION = []


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(random.choice(COLORS))
        self.x_move = 300
        self.speed(0.1)
        self.goto(x=self.x_move, y=0)

    def move(self):
        new_x = self.x_move - 30
        self.goto(x=new_x, y=0)


