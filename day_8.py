def get_message():
  msg = input('Enter a message to process... \n').lower()
  if len(msg) < 1:
    return get_message()
  return msg
  
def get_coding_mode():
  mode = input('ENCODE or DECODE ? \n')
  if mode != 'ENCODE' and mode != 'DECODE':
    return get_coding_mode()
  return mode

def process_message(mode, msg, shift):
  temp = []
  output = ''
  
  if mode == 'ENCODE':
    for char in msg:
      uni = ord(char) + shift
      if uni > 122:
        uni = uni - 26      
      temp.append(uni)
    
  elif mode == 'DECODE':
    for char in msg:
      uni = ord(char) - shift
      if uni < 97:
        uni = uni + 26  
      temp.append(uni)
      
  for x in temp:
    char = chr(int(x))
    output += char
    
  return output
  
def get_shift():
  shift = input('How many to shift? (digit) \n')
  try:
    return int(shift)
  except ValueError as e:
    print(e)
    return get_shift()
  
def app():
  msg = get_message()
  mode = get_coding_mode()
  shift = get_shift()
  output = process_message(mode, msg, shift)
  print(f"Here's your processed message: {output.upper()}")

app()
