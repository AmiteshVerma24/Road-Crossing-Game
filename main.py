#Importing required modules
from turtle import Screen , Turtle
from player import Player
from car import Car
from scoreboard import Scoreboard
import time

#Creating the screen object
my_screen = Screen()

#Setting up the screen
my_screen.setup(width = 600 , height = 600)
my_screen.title("Turtle Crossing Game")
my_screen.tracer(0)

#Creating the player object
player = Player()

#Making the screen to take user input
my_screen.listen()

#Taking input from user to move the turtle
my_screen.onkey(fun = player.move , key = "Up")

#Main body of the program
game_on = True

#Creating the car object
car = Car()
car.hideturtle()

#Creating the scoreboard
lvl = 1
scoreboard = Scoreboard()
steps = 10

while game_on:
    #Creating cars on the screen
    car.create()
    car.move(step_size = steps)

    #Detecting collision between car and the turtle
    for element in car.carlst:
        if player.distance(element) < 15:
            game_on = False

    #Checking if the player has reached the other side or not
    if player.ycor() > 300:
        player.restart()
        scoreboard.update_score()
        steps += 5

    #Updating details on the screen
    time.sleep(0.1)
    my_screen.update()


# Making the screen to exit on click
my_screen.exitonclick()
