high_bid = 0
high_bidder = ''
more_bidders = True

def get_bid():
  bidder = input('What is your name? \n')
  amount = int(input('How much? \n'))
  return {
    'bidder': bidder,
    'amount': amount,
  }

def update_high_bid(new_bid):
  global high_bid, high_bidder
  if int(new_bid['amount']) > high_bid:
    high_bid = int(new_bid['amount'])
    high_bidder = new_bid['bidder']

def are_more_bidders():
  res = input('Are there more bidders? (Y/N) \n')[0].upper()
  if res == 'Y':
    return True
  return False

def auction():
  global more_bidders
  while more_bidders:
    bid = get_bid()
    update_high_bid(bid)
    next_bidder = are_more_bidders()
    if not next_bidder:
      more_bidders = False
      print(f"The winner is {high_bidder} with a winning bid of {high_bid}")

auction()