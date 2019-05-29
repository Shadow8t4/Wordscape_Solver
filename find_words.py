# Find words based on letters given

from read_english_dictionary import load_words
from sys import argv

def create_bank(letters):
  lb = {}
  for l in letters:
    if(l in lb):
      lb[l] += 1
    else:
      lb[l] = 1
  
  return lb

def main(letters):
  wdb = load_words()

  for w in wdb:
    if(len(letters) >= len(w) and len(w) >= 3):
      lb = create_bank(letters)
      contains_letters = True
      for l in w:
        not_in = 0
        for t in lb.keys():
          if(l == t):
            if(lb[l] > 0):
              lb[l] -= 1
              #print(lb)
            else:
              #lb = lb
              contains_letters = False
          else:
            not_in += 1
        
        if(not_in == len(lb.keys())):
          contains_letters = False
      
      if(contains_letters):
        print(w)

if(__name__ == '__main__'):
  main('catlle')