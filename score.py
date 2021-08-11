from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.shape(None)
        self.speed(0)
        self.add_score()
        self.high_score = 0
        with open(file="data.txt") as data:
            self.high_score = int(data.read())

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER", align="center", font=("Courier", 30, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font = ("Courier", 20, "normal"))

    def add_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
