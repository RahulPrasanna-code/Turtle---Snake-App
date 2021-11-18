from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from bonusfood import BonusFood
import turtle
import time


screen=Screen()
screen.title("Snake Game")
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)

scoreboard = ScoreBoard()
snake = Snake()
food = Food()
bonusfood = BonusFood()


screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True


while game_is_on:
	screen.update()
	time.sleep(0.1)
	snake.move()


	if snake.head.distance(food)<15:
		food.refresh()
		scoreboard.increase_score()
		snake.extend()

	if scoreboard.score%3==0 and scoreboard.score>1 and not bonusfood.created:
		bonusfood.create()


	#collision with bigfood
	if bonusfood.created and snake.head.distance(bonusfood)<15:
		bonusfood.delete()
		scoreboard.bonus_score_increase()
		snake.extend()

	#collision with walls
	if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
		scoreboard.game_over()
		game_is_on = False

	#collision with body
	for segment in snake.segments[1:]:
		if snake.head.distance(segment)<10:
			scoreboard.game_over()
			game_is_on=False






screen.exitonclick()