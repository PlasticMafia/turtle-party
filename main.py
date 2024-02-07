# Turtle Party Project
# by River Moon
# 02.02.2024
import turtle
turtle.color("blue")

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
  
#forward helper function
def move(len):
  back(-1 * len)
  
def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.left(360 / num)
    
def spiral(len, angle):
  for i in range(len, 5, -5):
    turtle.forward(i)
    turtle.right(angle)
    
spiral(75, 45)
move(50)
turtle.color("red")
spiral(50, 90)
