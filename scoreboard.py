from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level_number = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(x = -230 , y = 260)
        self.write(arg = f"Level: {self.level_number}" , move = False , align = "center" , font = ("Arial" , 30 , "bold"))

    def update_score(self):
        self.clear()
        self.level_number += 1
        self.write_score()
    
    def write_score(self):
        self.write(arg = f"Level: {self.level_number}" , move = False , align = "center" , font = ("Arial" , 30 , "bold"))



    