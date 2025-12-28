import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)

player=Player()
car=CarManager()
scoreboard=Scoreboard()

screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkey(player.up,"Up")
    car.create_car()
    car.move()
    for cars in car.all_cars:
        if cars.distance(player)<15:
            scoreboard.game_over()
            game_is_on=False
        if player.ycor()>280:
            player.go()
            car.speed()
            scoreboard.inc()





screen.exitonclick()



