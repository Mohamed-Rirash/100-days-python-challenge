from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        

    def update_score_board(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align="center",font=("arial",70,"normal"))
        self.goto(100,200)
        self.write(self.r_score,align="center",font=("arial",70,"normal"))

    def l_poin(self):
        self.l_score += 1
        self.update_score_board()

    def r_poin(self):
        self.r_score += 1
        self.update_score_board()