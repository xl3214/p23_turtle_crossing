from random import randint
from turtle import Turtle

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()
        self.steps = 0

    def create_car(self):
        self.shape("square")
        self.up()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(COLORS[randint(0, 5)])
        self.goto(300, randint(-250, 251))

    def move(self):
        new_x = self.xcor() - (STARTING_MOVE_DISTANCE + self.steps * MOVE_INCREMENT)
        if new_x > -300:
            self.goto(new_x, self.ycor())
        else:
            self.refresh()

    def refresh(self):
        self.goto(300, self.ycor())
        self.move()

    def speed_up(self):
        self.steps += MOVE_INCREMENT

