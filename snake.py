from turtle import Turtle

SEGMENT_POSITIONS = [(20, 0), (0, 0), (-20, 0)]

MOVE_DISTANCE = 20

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake(Turtle):
	def __init__(self):
		self.segments = []
		self.create()
		self.head = self.segments[0]

	def create(self):
		for each_square in SEGMENT_POSITIONS:
			self.add_segment(each_square)

	def extend(self):
		position=self.segments[-1].position()
		self.add_segment(position)

	def add_segment(self,position):
		self.segment = Turtle("square")
		self.segment.color("white")
		self.segment.penup()
		self.segment.goto(position)
		self.segments.append(self.segment)

	def move(self):
		for seg_num in range(len(self.segments)-1,0,-1):
			x_cor = self.segments[seg_num-1].xcor()
			y_cor = self.segments[seg_num-1].ycor()
			self.segments[seg_num].goto(x_cor,y_cor)
		self.head.forward(MOVE_DISTANCE)




	def up(self):
		if self.head.heading() != DOWN:
			self.head.setheading(UP)

	def down(self):
		if self.head.heading() != UP:
			self.head.setheading(DOWN)

	def left(self):
		if self.head.heading() != RIGHT:
			self.head.setheading(LEFT)

	def right(self):
		if self.head.heading() != LEFT:
			self.head.setheading(RIGHT)