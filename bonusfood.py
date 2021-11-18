from turtle import Turtle
from random import randint

class BonusFood(Turtle):
	def __init__(self):
		super().__init__()
		self.created = False
		self.deleted = True

	def create(self):
		if self.created:
			pass
		else:
			self.shape("circle")
			self.penup()
			self.shapesize(1,1)
			self.color("blue")
			self.speed("fastest")
			x_cor = randint(-280,280)
			y_cor = randint(-280,280)
			self.goto(x_cor,y_cor)
			self.created=True
			self.deleted = False
		

	def delete(self):	
		self.created = False
		self.deleted = True
		self.goto(400,400)

