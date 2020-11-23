from random import choice
from higher_lower_game_data import data

def get_data():
  return data

def get_next(data):
  if len(data):
    return choice(data)
  return False

def compare(guess, target_one, target_two):
  if guess == 'A':
    if target_one['follower_count'] > target_two['follower_count']:
      return True
  else:
    if target_one['follower_count'] < target_two['follower_count']:
      return True
  print('Wrong!')
  return False

def print_question(target_one, target_two):
  print(f"Who has a bigger follower count: (A) {target_one['name']} or (B) {target_two['name']}? ")

def get_guess():
  guess = input('Your guess? ').upper()
  if guess != 'A' and guess != 'B':
    return get_guess()
  return guess

def game():
  print('Welcome to the Higher or Lower Game')
  score = 0
  game_on = True
  data = get_data()
  target_one = get_next(data)
  
  while game_on:
    old_one = target_one or None
    target_one = old_one
    target_two = get_next(data)
    if target_one in data:
      data.remove(target_one)
    data.remove(target_two)
    print_question(target_one, target_two)
    guess = get_guess()
    game_on = compare(guess, target_one, target_two)
    if game_on:
      score += 1
      print(f"Score: {score}")
    target_one = target_two
    
game()
    