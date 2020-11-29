# # list comp

# from os import sched_get_priority_max


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# doubles = [n * 2 for n in numbers]

# capped = [letter.upper() for letter in 'Brandon']

# dict = {
#   'name': 'brandon',
#   'age': 39
# }

# valz = [dict[key] for key in dict]

# ran = [n * 2 for n in range(1, 6)]

# evens = [n for n in numbers if n % 2 == 0]

# with open('file_1.txt') as file_1:
#   numbers_1 = [int(n) for n in file_1]
#   file_1.close()
# with open('file_2.txt') as file_2:
#   numbers_2 = [int(n) for n in file_2]
#   file_2.close()
# result = [n for n in numbers_1 if n in numbers_2]

# # dict comp
# from random import randint
# names = ['alex', 'brandon', 'timmy turtle', 'samantha cat', 'ellie pup']
# scores = {name:randint(1, 101) for name in names}
# complex = [{name:randint(1, 101)} for name in names]


# phrase = "what is the airspeed velocity of an unladen swallow?"
# result = {word.title():len(word) for word in phrase.split()}


# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {k:(v * 9/5) + 32 for (k, v) in weather_c.items()}  

import pandas as pd
with open('nato_phonetic_alphabet.csv') as alphabet_file:
  alphabet_df = pd.read_csv(alphabet_file)  
alphabet = {row['letter']:row['code'] for (idx, row) in alphabet_df.iterrows()}

input = input('enter name... ').upper()
# input_dict = {letter:alphabet[letter] for letter in input}
input_list = [alphabet[letter] for letter in input]
print(' '.join(input_list))

