from random import choice
from os import system
from card_deck import deck

dealer_hand = []
dealer_score = 0
player_hand = []
player_score = 0

def draw_card():
  card = choice(game_deck)
  game_deck.remove(card)
  return card

# def update_score(score, hand):
#   if score > 21:
#     if 11 in hand:
#       return 

def dealer_hit(score):
  if score >= 17:
    return False
  return True

def player_hit():
  decision = input('HIT or STAY? ').upper()[0]
  if decision == 'H':
    return True
  elif decision == 'S':
    return False
  else:
    return player_hit()
  

def deal():
  global dealer_hand, player_hand, game_deck
  game_deck = deck
  for card in game_deck:
    card['visible'] = False
  
  dealer_hand = []
  player_hand = []
  
  player_face_up = draw_card()
  player_face_up['visible'] = True
  player_hand.append(player_face_up)
  player_hand.append(draw_card())
  
  dealer_face_up = draw_card()
  dealer_face_up['visible'] = True
  dealer_hand.append(dealer_face_up)
  dealer_hand.append(draw_card())
  
def update_score(hand):
  score = 0
  ace_in_hand = False
  for card in hand:
    if card['name'] == 'Ace':
      ace_in_hand = True
    score += card['value']
  if score > 21 and ace_in_hand:
    score -= 10
  return score
    
def print_hands(dealer_show=False):
  system('clear')
  if dealer_show:
    print(f"Dealer Score: {dealer_score}")
    for card in dealer_hand:
      card['visible'] = True
  print('Dealer Has: ')
  for card in dealer_hand:
    if card['visible']:
      display = f"{card['name']} of {card['suit']}"
    else:
      display = 'X of X'
    print(display)
    
  print('🃏  ' * 6)
    
  print('Player Has: ')
  print(f"Player Score: {player_score}")
  for card in player_hand:
      display = f"{card['name']} of {card['suit']}"
      print(display)

def game():
  global player_hand, dealer_hand, player_score, dealer_score
  dealer_alive = True
  player_alive = True
  player_playing = True
  deal()
  dealer_score = update_score(dealer_hand)
  player_score = update_score(player_hand)
  print_hands()
  
  while dealer_alive and player_alive and player_playing:
    if dealer_hit(dealer_score):
      dealer_hand.append(draw_card())
      dealer_score = update_score(dealer_hand)
      if dealer_score > 21:
        dealer_alive = False
    if player_hit():
      player_hand.append(draw_card())
      player_score = update_score(player_hand)
      if player_score > 21:
        player_alive = False
    else:
      player_playing = False
    print_hands(True)
    
  print_hands(True)
  if not dealer_alive:
    print('Player Wins! ')
  elif not player_alive:
    print('Dealer Wins... ')
  elif player_score > dealer_score:
    print('Player Wins! ')
  elif dealer_score > player_score:
    print('Dealer Wins...')
  elif dealer_score == player_score:
    print('Draw...')
    
  play_again = input('Play again? (Y/N)').upper()
  if play_again == 'Y':
    return game()
  else:
    return
    
game()  