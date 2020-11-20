from random import choice

armoury = ['R', 'P', 'S']

def get_player_weapon():
  weapon = input('Choose your weapon... (R, P or S) \n').upper()
  if weapon in armoury:
    return weapon
  else:
    return get_player_weapon()
  
def get_computer_weapon():
  return choice(armoury)

def find_winner(player_weapon, computer_weapon):
  print(f"Computer chose {computer_weapon}")
  if player_weapon == 'R':
    if computer_weapon == 'R':
      return 'Tie'
    elif computer_weapon == 'P':
      return 'Computer Wins!'
    else:
      return 'You Win!'
  elif player_weapon == 'P':
    if computer_weapon == 'R':
      return 'You Win!'
    elif computer_weapon == 'P':
      return 'Tie'
    else:
      return 'Computer Wins!'
  else:
    if computer_weapon == 'R':
      return 'Computer Wins!'
    elif computer_weapon == 'P':
      return 'You Win'
    else:
      return 'Tie'
    
def intro():
  print('Welcome to Rock, Paper, Scissors!')
    
def game():
  intro()
  computer_weapon = get_computer_weapon()
  player_weapon = get_player_weapon()
  res = find_winner(player_weapon, computer_weapon)
  print(res)
  play_again = input(f"Play again? (Y/N)").upper()
  if(play_again == 'Y'):
    return game()
  return
  
game()
  