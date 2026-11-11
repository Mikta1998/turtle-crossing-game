from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.color("white")
        self.hideturtle()
        self.goto(-290, 270)
        self.display_score()

    def increase_level(self):
        self.level += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def display_score(self):
        self.write(f"Level: {self.level}",
                    move=False,
                    font=FONT)
