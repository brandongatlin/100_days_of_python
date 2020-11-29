from turtle import Turtle, Screen
from random import randint

screen = Screen()
timmy = Turtle()
timmy.shape('turtle')
timmy.color('red')
timmy.pencolor('green')
penwidth = 5
timmy.width(width=penwidth)

# random path
turns = [timmy.left, timmy.right]
def random_turtle_move():
  times = randint(1, 3)
  global penwidth
  penwidth += 1
  timmy.width(width=penwidth)
  timmy.forward(25)
  for _ in range(1, times):
    turns[randint(0, 1)](90)
  

for _ in range(1, 10):
  random_turtle_move()


# # dashed line
# for move in range(1, 5):
#   timmy.pendown()
#   timmy.forward(10)
#   timmy.pu()
#   timmy.forward(5)

# all geo shapes
# def draw_turtle_shape(num_sides, length_of_side):
#   ang = 360 / num_sides
#   for _ in range(1, num_sides + 1):
#     timmy.forward(length_of_side)
#     timmy.left(ang)

# for num in range(3, 10):
#   draw_turtle_shape(num, 90)












screen.exitonclick()
