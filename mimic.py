import random
import sys


def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  dictionary = {}
  file_content = open(filename,'r')
  file_read = file_content.read()
  file_content.close()
  content_lower = file_read.lower()
  content = content_lower.split()
  for words in content:
   if words not in dictionary.keys() and content[-1]!= words:
    #print words
    value_dict= content[content.index(words)+1]
    dictionary[words] = value_dict
  #print dictionary
  return


def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  # have not started on this yet
  return



def main():
  if len(sys.argv) != 2:
    print 'usage: ./mimic.py file-to-read'
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
