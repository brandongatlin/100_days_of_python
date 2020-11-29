# pong
from turtle import Turtle, Screen, onkey
screen = Screen()
screen.setup(width=500, height=400)
screen.register_shape("paddle", ((0,0), (50,0), (50,2), (0,2)))
screen.register_shape("ball", ((0,0), (50,0), (50,2), (0,2)))
screen.listen()

class Paddle(Turtle):
  def __init__(self, side):
    super().__init__()
    self.shape('paddle')
    self.side = side
    self.x = 0
    self.y = 0
    
  def reset(self):
    self.penup()
    if self.side == 'L':
      self.x = -200
      self.setx(self.x)
    else:
      self.x = 200
      self.setx(self.x)
    self.y = 25
    self.sety(self.y)
      
  def up(self):
    self.y += 20
    self.sety(self.y)
    
  def down(self):
    self.y -= 20
    self.sety(self.y)
    
  def get_x(self):
    return self.xcor()
  
  def get_y(self):
    return self.ycor()
    

class Ball(Turtle):
  def __init__(self, size, color):
    self.shape('ball')
    self.size = size
    self.color = color
    self.x = 0
    self.y = 0
    self.dir = ''
    
    self.resizemode('user')
    self.shapesize(size)
    self.fillcolor(color)
    self.speed(1)
    self.penup()
    
  def get_x(self):
    return self.xcor()
  
  def get_y(self):
    return self.ycor()
  
  def move(self, dir):
    print('move called')
    
    if dir == 'L':
      self.forward(-500)
      self.dir = 'R'
    else:
      self.forward(500)
      self.dir = 'L'
          

    
    
def start_game():
  ball = Ball(1, 'red')
  left_paddle = Paddle('L')
  right_paddle = Paddle('R')
  left_paddle.reset()
  right_paddle.reset()
  onkey(right_paddle.up, 'Up')
  onkey(right_paddle.down, 'Down')
  
  ball.move('L')
  ball_moving = True
  
  while ball_moving:
    print(ball.get_x())
    if ball.get_x() < 10 or ball.get_x() > 240:
      print('touch')
      if ball.dir == 'L':
        ball.dir = 'R'
      else:
        ball.dir = 'L'
      ball.move(ball.dir)
    
    
      
    
  
  
start_game()












screen.exitonclick()