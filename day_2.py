# score = 0
# height = 1.5
# is_winning = False
# status = 'You are winning' if is_winning else 'You are losing'

# output = f'Score: {score}, Height: {height}, {status}'
# print(output)

# tip calc
allowable_percentages = [.1, .15, .18]

def get_total_bill():
  bill_total = input('What was your total bill? ')
  try:
    bill_total = float(bill_total)
    if bill_total > 0:
      return bill_total
  except ValueError as e:
    print(e)
  return get_total_bill()

def get_tip_percentage():
  chosen_tip_percentage = input('What tip percentage do you want to give? (.10, .15 or .18) ')
  try:
    chosen_tip_percentage = float(chosen_tip_percentage)
    if chosen_tip_percentage in allowable_percentages:
      return chosen_tip_percentage
  except ValueError as e:
    print(e)
  return get_tip_percentage()
  
def get_number_diners():
  number_diners = input('How many diners do you want to split the check with? (> 0) ')
  try:
    number_diners = int(number_diners)
    if number_diners > 0:
      return number_diners
  except ValueError as e:
    print(e)
  return get_number_diners()
  
def calculate_tip(total, tip_percent, num_diners):
  return ((total * tip_percent) + total) / num_diners
  
# APP
print('Welcome to the Tip Calculator ')
total_bill = get_total_bill()
chosen_tip_percentage = get_tip_percentage()
number_diners = get_number_diners()
split_total = round(calculate_tip(total_bill, chosen_tip_percentage, number_diners), 2)
print(f'${split_total}')








