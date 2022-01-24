from turtle import Turtle
import random

COLOUR = ["red" , "blue" , "green" , "yellow" , "orange" , "pink"]

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.carlst = []

    def create(self):
        num = random.randint(1 , 5)
        if num == 3:
            car = Turtle()
            car.color(random.choice(COLOUR))
            car.shape("square")
            car.penup()
            car.setheading(180)
            random_y = random.randint(-240 , 250)
            car.goto(x = 260 , y = random_y)
            car.shapesize(stretch_len = 2 , stretch_wid = 1)
            self.carlst.append(car)
        
    def move(self , step_size):
        for element in self.carlst:
            new_x = element.xcor() - step_size
            element.goto(x = new_x , y = element.ycor())