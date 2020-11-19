from time import sleep

def pluralize(input):
  if input.lower().endswith('s'):
    return f'{input}es'
  elif input.lower().endswith('y'):
    return f'{input[:len(input) - 1]}ies'
  else:
    return f'{input}s'

print('hello user. I will construct a band name for you.')
city = input('what city did you grow up in?')
pet = input('what is the name of a pet you had/have?')
print('thinking...')
sleep(3)
print(f'Your band name is The {city} {pluralize(pet)}')
