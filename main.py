import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.bgcolor("black")
cars = []
player = Player()
level = Scoreboard()

for _ in range(30):
    cars.append(CarManager())

screen.onkey(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.ycor() > 280:
        player.refresh()
        level.increase_level()
        for car in cars:
            car.reposition()
            car.increase_speed()
    for car in cars:
        if car.xcor() > -320:
            car.move()
        else: car.reposition()
    for car in cars:
        if player.distance(car) < 20:
            level.game_over()
            game_is_on = False

screen.exitonclick()