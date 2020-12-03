from random import shuffle

class Deck:
  def __init__(self, word_list):
    self.word_list = [Flashcard('English', 'Latin', card['en'], card['la'], False) for card in word_list]
    
  def shuffle(self):
    self.word_list.shuffle()
    
  def get_unknowns(self):
    return [card for card in self.word_list if not card.known]

class Flashcard:
  def __init__(self, l1, l2, l1_word, l2_word, known):
    self.l1 = l1
    self.l2 = l2
    self.l1_word = l1_word
    self.l2_word = l2_word
    self.known = known
    
  def __str__(self):
    return f"{self.l2_word} is {self.known}"
    
  def learn(self):
    self.known = True