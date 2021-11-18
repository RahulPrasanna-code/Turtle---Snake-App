from turtle import Turtle

FONT_STYLE=("ALGERIAN", 24, "normal")


class ScoreBoard(Turtle):
	def __init__(self):
		super().__init__()
		self.score=0
		self.color("white")
		self.hideturtle()
		self.penup()
		self.goto(0,270)
		self.update_score()

	def update_score(self):
		self.write(f"Score:{self.score}",align="center",font=FONT_STYLE)

	def increase_score(self):
		self.score+=1
		self.clear()
		self.update_score()

	def bonus_score_increase(self):
		self.score+=3
		self.clear()
		self.update_score()

	def game_over(self):
		self.goto(0,0)
		self.write("Game Over" , align="center", font=FONT_STYLE)