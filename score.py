from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open(file="data.txt") as data:
            self.high_score = int(data.read())
        self.score = -1
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.shape(None)
        self.speed(0)
        self.add_score()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", move=False, align="center", font = ("Courier", 20, "normal"))

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # Rewrite text file with high score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align="center", font=("Courier", 30, "normal"))
        self.goto(0, -20)
        self.write("Click the space bar to go again.", align="center", font=("Courier", 15, "normal"))
        self.goto(0, -40)
        self.write("Click the screen to exit.", align="center", font=("Courier", 15, "normal"))

    def add_score(self):
        self.score += 1
        self.update_scoreboard()
