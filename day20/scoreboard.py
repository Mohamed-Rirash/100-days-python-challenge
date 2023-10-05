from turtle import Turtle

ALIENMENT = "center"
FONT = ("Roboto", 15, "normal")  # Updated font name to "Roboto"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0  # Initialize high score to 0 initially

        # Read the high score from the data.txt file
        with open("day20/data.txt", "r") as data:
            self.high_score = int(data.read())

        self.penup()
        self.color("white")
        self.goto(0, 360)
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIENMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score_board()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        # Write the new high score back to the data.txt file
        with open("day20/data.txt", "w") as data:
            data.write(str(self.high_score))

        self.score = 0
        self.update_score_board()
