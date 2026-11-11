from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.penup()
        self.spawn_position_x = random.choice(list(range(310,1500)))
        self.spawn_position_y = random.choice(list(range(-270,270)))
        self.goto(self.spawn_position_x, self.spawn_position_y)
        self.turtle_speed = STARTING_MOVE_DISTANCE
        self.speed_increment = MOVE_INCREMENT

    def move(self):
        self.forward(self.turtle_speed)

    def reposition(self):
        self.spawn_position_x = random.choice(list(range(310,1500)))
        self.spawn_position_y = random.choice(list(range(-270, 270)))
        self.goto(self.spawn_position_x, self.spawn_position_y)

    def increase_speed(self):
        self.turtle_speed += self.speed_increment

