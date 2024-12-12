
# P4LAB1
# Bailey_Elijah
# 10/29/24
# Use loops and turtle library to draw a house
# Import turtle library
import turtle
# Set up the window and turtle object
window = turtle.Screen()
tom = turtle.Turtle()
# Change features of turtle
tom.pensize(10)
tom.pencolor("purple")
tom.shape("arrow")
# While loop that runs 4 times
movement = 0

while movement <= 3:
    movement += 1
    tom.forward(150)
    tom.right(90)
    
# For loop to run 3 times
for side in range(3):
    tom.forward(150)
    tom.left(120)
