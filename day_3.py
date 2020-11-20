score = 0

def intro():
  print('Welcome to Treasure Island')
  print('Choose your steps carefully...')
  print('Type the command you want to do...')
  
def game_over():
  print(f"Game over!")
  score = 0
  wants_to_play_again = input(f"Do you want to play again? (YES/NO)\n").upper()[0]
  if wants_to_play_again == 'Y':  
    game()
  else:
    return
  
def step(message, possibles_moves):
  possibles_moves.append('\n')
  print(message)
  print('Which do you choose? ')
  return input(', '.join(possibles_moves)).upper()[0]
  

def game():
  intro()
  
  move_one = step(f"You've arrived at a house", ['ENTER, RUN, CELLAR'])
  if move_one == 'E':
    global score
    score += 1
    print(f"You're safe for now... Your score is now {score}")
  elif move_one == 'R':
    print(f"You've been caught in a beartrap and succumbed to your injuries...")
    game_over()
  elif move_one == 'C':
    print(f"You tripped and fell down into the dungeon. Luckily, you died from the fall and won't be tortured to death.")
    game_over()
  else:
    print(f"Wrong move - You've been killed due to your indecision. ")
    game_over()
    
  move_two = step(f"You're in the dining room. ", ['LEFT', 'RIGHT', 'STRAIGHT'])
  if move_two == 'L':
    print(f"You've been eaten by cannibals...")
    game_over()
  elif move_two == 'R':
    score += 1
    print(f"You're safe for now... Your score is now {score}")
  elif move_two == 'S':
    print(f"You've stubbed your toe and died of infection.")
    game_over()
  else:
    print(f"Wrong move - You've been killed due to your indecision. ")
    game_over()
    
  move_three = step(f"You've entered the study.", ['UPSTAIRS', 'DOWNSTAIRS', 'WORK on your caligraphy'])
  if move_three == 'W':
    print(f"You've died of bordem.")
  elif move_three == 'U':
    print(f"Grandma has turned you into a lampshade.")
  elif move_three == 'D':
    score += 1
    print(f"You've found the treasure - your score is {score}")
  else:
    print(f"Wrong move - You've been killed due to your indecision. ")

  game_over()

game()

  