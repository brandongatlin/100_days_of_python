from random import choice

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def generate_random(list):
  return choice(list)

def get_length(list):
  return int(input(f"How many {list} do you want? "))

def app():
  print('Welcome to the random password generator - answer the questions to customize your password')
  num_letters = get_length('letters')
  num_symbols = get_length('symbols')
  num_numbers = get_length('numbers')
  
  randoms = []
  password = ''
  
  for _ in range(1, num_letters + 1):
    randoms.append(choice(letters))
  for _ in range(1, num_symbols + 1):
    randoms.append(choice(symbols))
  for _ in range(1, num_numbers + 1):
    randoms.append(str(choice(numbers)))
    
  for _ in range(0, len(randoms)):
    rand = choice(randoms)
    password += rand
    randoms.remove(rand)
  return password
  

print(app())