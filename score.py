from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("./Score/highscore.txt") as file:
            self.highscore = int(file.read())
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  Highscore:{self.highscore} ", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.color("#EE4B2B")
        self.write(f"Game Over!", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_score()
            
