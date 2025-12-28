FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()

        self.penup()
        self.goto(-280,260)
        self.inc()


    def inc(self):

        self.upd()
        self.level += 1

    def upd(self):
        self.clear()
        self.write(f"level:{self.level}")

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)



