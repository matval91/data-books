# functions to analyse the words inside a book
#
# M. Vallar - 09/2023

import numpy as np 
import re

def repeat_words(book, n_words=10):
	"""
	Counts the words 
	""" 
  book_list = book.split()
  unique_words = np.unique(book_list)
  unique_dict=dict()
  regex = re.compile('[^a-zA-Z0-9 -]')
  for ii in unique_words:
    ii=regex.sub('', ii)
    unique_dict[ii]=book_list.count(ii)