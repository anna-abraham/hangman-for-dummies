import random

class Hangman:
  states = [
    '''
    _______
    |     |
    |     |
    |     
    |    
    |    
    |         
    ''',
    '''
    _______
    |     |
    |     |
    |     O
    |    
    |    
    |         
    ''',
    '''
    _______
    |     |
    |     |
    |     O
    |     :
    |    
    |         
    ''',
    '''
    _______
    |     |
    |     |
    |     O
    |    <:
    |    
    |         
    ''',
    '''
    _______
    |     |
    |     |
    |     O
    |    <:>
    |    
    |         
    ''',
    '''
    _______
    |     |
    |     |
    |     O
    |    <:>
    |    /
    |         
    ''',
    '''
    _______
    |     |
    |     |
    |     O
    |    <:>
    |    / \\
    |         
    '''
  ]

  def __init__(self):
    word_list = ["dizziness", "precedent", "crossjack", "stratiformis", \
    "cumbersomeness", "schizogamy", "insolvably", "jobbery", "painless", "uncontestant"]

    self.word = random.choice(word_list)
    self.status = 0

  def increase(self):
    if self.status < 6:
      self.status += 1

    else:
      return False

  def print_status(self):
    print(self.states[self.status])

  def print_word(self):
    print(self.word)

