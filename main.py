from turtle import Screen
import time
from snek import Snek
from food import Food
from score_board import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snek Game")
screen.tracer(0)

snek = Snek()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snek.up, "Up")
screen.onkey(snek.down, "Down")
screen.onkey(snek.left, "Left")
screen.onkey(snek.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snek.move()

    # Detect Collision with Food
    if snek.head.distance(food) < 15:
        food.refresh()
        snek.extend()
        scoreboard.increase_score()

    # Detect Collision with Wall
    if snek.head.xcor() > 290 or snek.head.xcor() < -290 or snek.head.ycor() > 290 or snek.head.ycor() < -290:
        scoreboard.gameover()
        print("ITS OVER")
        game_is_on = False

    # Detect Collision with Tail
    for segment in snek.segments[1:]:
        if snek.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.gameover()

screen.exitonclick()
