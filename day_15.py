from os import system
# from coffees import MENU

class Coffee_Machine:
  def __init__(self, name:str, water:int, milk:int, coffee:int, change:float):
    self.name = name
    self.water = water
    self.milk = milk
    self.coffee = coffee
    self.change = change
    self.stock = ['E', 'L', 'C']
    self.espreso_reqs = {
      'water': 50,
      'milk': 0,
      'coffee': 18,
      'price': 1.0,
    }
    self.latte_reqs = {
      'water': 200,
      'milk': 150,
      'coffee': 24,
      'price': 1.5,
    }
    self.cappuccino_reqs = {
      'water': 250,
      'milk': 100,
      'coffee': 24,
      'price': .75,
    }
    
  def turn_off(self):
    quit()
    
  def get_reqs(self, choice):
    if choice == 'E':
      return self.espreso_reqs
    elif choice == 'L':
      return self.latte_reqs
    elif choice == 'C':
      return self.cappuccino_reqs
    
  def prompt_user(self):
    coffee = input('What would you like: ESPRESSO, LATTE or CAPPUCCINO? ').upper()[0]
    if coffee not in self.stock:
      return self.prompt_user()
    return coffee
  
  def water_sufficient(self, amount):
    if amount > self.water:
      return False
    return True
  
  def milk_sufficient(self, amount):
    if amount > self.milk:
      return False
    return True
  
  def coffee_sufficient(self, amount):
    if amount > self.coffee:
      return False
    return True
  
  def change_sufficient(self, amount):
    if amount > self.change:
      return False
    return True
      
  def resources_sufficient(self, choice):
    requirements = self.get_reqs(choice)
      
    if not self.water_sufficient(requirements['water']):
      return False
    if not self.milk_sufficient(requirements['milk']):
      return False
    if not self.coffee_sufficient(requirements['coffee']):
      return False
    return True
  
  def adjust_resources(self, choice):
    requirements = self.get_reqs(choice)
    self.water -= requirements['water']
    self.milk -= requirements['milk']
    self.coffee -= requirements['coffee']
    self.change -= requirements['price']
    self.report()
  
  def report(self):
    output = f"""
      The {self.name} currently has:
      {self.water} ml of Water
      {self.milk} ml of Milk
      {self.coffee} g of Coffee
      ${self.change} in Change
    """
    print(output)
    
  def take_money(self, choice):
    requirements = self.get_reqs(choice)
    print(f"Please insert ${requirements['price']} usings quarters only")
    quarters_in = input('How many quarters are you putting in? ')
    try:
      return int(quarters_in * 25)
    except ValueError as e:
      print(e)
      return self.take_money()
    
machine = Coffee_Machine('BG-1000', 300, 300, 300, 10.5)
machine_on = True

while machine_on:
  choice = machine.prompt_user()
  reqs = machine.get_reqs(choice)
  
  if not machine.resources_sufficient(choice):
    print('Sorry Insufficient Resources...')
    choice = machine.prompt_user()
  else:
    inserted = machine.take_money(choice)
    if inserted < reqs['price']:
      print('Not enough money given - I\'m keeping it')
      machine.turn_off()
    machine.adjust_resources(choice)
