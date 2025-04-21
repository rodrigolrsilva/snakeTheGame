from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.current_score = 0
        self.write(arg=f"Score: {self.current_score}", align="center", font =('Chilanka', 15, 'normal'))
    def write_score(self):
        self.clear()
        self.write(arg=f"Score: {self.current_score}", align="center", font =('Chilanka', 15, 'normal'))

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write(arg="GAME OVER", align="center", font=("Comic Sans", 20, 'normal'))