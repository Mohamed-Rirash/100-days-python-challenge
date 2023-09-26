from turtle import Turtle
ALIENMENT = "center"
FONT = ("roboto", 15 ,"normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0,360)
        self.hideturtle()
        self.update_score_board()

        
    def update_score_board(self):
        self.write(arg= f"score:{self.score}",move=False, align=ALIENMENT,font=FONT)
        

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg= f"score:{self.score}",move=False, align=ALIENMENT,font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write(arg= f"GAME OVER!",move=False, align=ALIENMENT,font=FONT)
