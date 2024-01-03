from turtle import Turtle
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
START_POS = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.up()
        self.setheading(90)
        self.goto(START_POS)
        self.has_restarted = False

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        if new_y < FINISH_LINE_Y:
            self.goto(self.xcor(), new_y)
        elif new_y >= FINISH_LINE_Y:
            self.restart()

    def restart(self):
        self.goto(START_POS)
        self.has_restarted = True
