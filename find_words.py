# Find words based on letters given

from import_dictionary import load_words
from sys import argv

def create_bank(letters):
  lb = {}
  for l in letters:
    if(l in lb):
      lb[l] += 1
    else:
      lb[l] = 1
  
  return lb

def main(letters, no_three=False):
  wdb = load_words()

  mininum = 3
  if(no_three):
    mininum += 1

  for w in wdb:
    if(len(letters) >= len(w) and len(w) >= mininum):
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
  if(len(argv) > 1):
    if(len(argv) > 2):
      if(argv[2] == '--no-three' or argv[2] == '-n'):
        main(argv[1], True)
      elif(argv[1] == '--no-three' or argv[1] == '-n'):
        main(argv[2], True)
      else:
        print('Usage: python find_words.py [letters] [-n | --no-three]')
    else:
      main(argv[1])
  else:
    print('Usage: python find_words.py [letters] [-n | --no-three]')