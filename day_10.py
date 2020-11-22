import operator, sys

def calculate(math_operator, num1, num2):
  ops = {
  '+': operator.add,
  '-': operator.sub,
  '*': operator.mul,
  '/': operator.truediv,
}
  return ops[math_operator](num1, num2)
  
def get_operator():
  """returns string of mathematical operator based on user input"""
  operators = ['+', '-', '*', '/']
  chosen_operator = input('Choose and operator (+ - * /) ')
  if chosen_operator not in operators:
    return get_operator()
  return chosen_operator

def get_number_input(operator=None):
  res = float(input('Enter the number '))
  if operator == '/' and res == 0:
    print('Cannot divide by 0 ')
    return get_number_input()
  return res
  

def continue_calculation(current_value):
  res = input(f'Type YES to continue calcuating with {current_value}, type NO to start a new calculation or type END to end the program ')[0].upper()
  if res == 'Y':
    return True
  elif res == 'E':
    sys.exit()
  else:
    return False
  
def calculator():
  still_calculating = True
  temp = 0
  
  while still_calculating:
    
    if temp == 0:
      num_one = get_number_input()
    else:
      num_one = temp
    operator = get_operator()
    num_two = get_number_input(operator)
    temp = calculate(operator, num_one, num_two)
    print(temp)
    still_calculating = continue_calculation(temp)
    
  calculator()
    
calculator()
  
  