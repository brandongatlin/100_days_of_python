from random import choice
from os import system

modes = [
  {
    'mode': 'easy',
    'attempts': 10,
  },
  {
    'mode': 'medium',
    'attempts': 7,
  },
  {
    'mode': 'hard',
    'attempts': 5,
  },
]

def create_numbers():
  numbers = []
  for num in range(1, 101):
    numbers.append(num)
  return numbers

def get_random(list):
  return choice(list)

def get_mode():
  mode = input('Would you like to play on EASY, MEDIUM OR HARD? Or RANDOM if you feel lucky... ').upper()[0]
  if mode == 'E':
    return modes[0]
  elif mode == 'M':
    return modes[1]
  elif mode == 'H':
    return modes[2]
  elif mode == 'R':
    return choice(modes)
  return get_mode()

def get_guess():
  guess = input('Take a guess => ')
  try:
    return int(guess)
  except ValueError as e:
    print(e)
    return get_guess()
  
def compare(answer, guess):
  if guess == answer:
    return f"You Win - the answer was {answer} and you guessed {guess}!"
  elif guess > answer:
    return f"{guess} is too HIGH"
  elif guess < answer:
    return f"{guess} is too LOW"
  
def replay():
  res = input('Would you like to play again? (Y/N)').upper()[0]
  if res == 'Y':
    return True
  return False
  
def game():
  game_on = True
  attempts = get_mode()['attempts']
  numbers = create_numbers()
  print("I'm thinking of a number between 1 and 100 ...")
  answer = get_random(numbers)
  
  while game_on and attempts > 0:
    guess = get_guess()
    res = compare(answer, guess)
    print(res)
    if 'too' in res:
      attempts -= 1
    elif 'Win' in res:
      game_on = False
    
    if attempts < 1:
      print('You lose...')
    else:
      print(f"Attempts Remaining: {attempts}")
      
  if replay():
    system('clear')
    return game()
game()
  
