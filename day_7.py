from random import choice
import word_bank

guessed_list = []
lives = 3

def pull_random_word():
  pulled = choice(word_bank.word_list())
  return pulled

def get_player_guess():
  return input('Guess a letter ').lower()

def check_guess(guess, word):
  if guess in word:
    return True
  return False

def print_word_status(word):
  for letter in word:
    if letter in guessed_list:
      print(letter)
    else:
      print(' - ')
      
def won(word):
  res = True
  for letter in word:
      if letter not in guessed_list:
        res = False
  return res
        
      
def game():
  global lives

  print('welcome to hangman, choose a letter.')
  word = pull_random_word()
  print(f"You're word has {len(word)} letters and you have {lives} lives.")
  game_over = False
  
  while not game_over:
    
    guess = get_player_guess()
    if guess not in guessed_list:
      guessed_list.append(guess)
      guessed_right = check_guess(guess, word)
      print_word_status(word)

      if not guessed_right:
        lives -= 1
        print(f"You have {lives} lives remaining.")
      if lives < 1:
        print('You lost!')
        game_over = True
      if won(word):
        print('You won!')
        game_over = True
    
    
game()
  
  