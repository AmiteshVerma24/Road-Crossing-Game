from turtle import Turtle
STARTPOINT = (0 , -280)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.speed("fastest")
        self.goto(STARTPOINT)
        
    def move(self):
        steps = 10
        self.forward(steps)

    def restart(self):
        self.goto(STARTPOINT)