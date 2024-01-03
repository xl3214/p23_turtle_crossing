from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"


class ScoreBoard(Turtle):
    """Create a scoreboard and count scores"""
    def __init__(self, position=(-270, 270)):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.up()
        self.goto(position)
        self.update()

    def update(self):
        self.write(f"Level: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

