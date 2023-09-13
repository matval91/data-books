# functions to analyse the words inside a book
#
# M. Vallar - 09/2023

import numpy as np 
import re
import operator

stop_words = [
    "a", "an", "and", "as", "at", "but", "by", "for", "if", "in", "it", "of",
    "on", "or", "the", "to", "with"
]

def repeat_words(book, n_words=10):
	"""
	Counts the words 
	""" 
  book_list = book.split()
  unique_words = np.unique(book_list)
  unique_words = [word for word in unique_words if word not in stop_words]

  unique_dict=dict()
  regex = re.compile('[^a-zA-Z0-9 -]')
  for ii in unique_words:
    ii=regex.sub('', ii)
    unique_dict[ii]=book_list.count(ii)

  sorted_d = dict( sorted(unique_dict.items(), key=operator.itemgetter(1),reverse=True))


def use_wordcloud(book):
  """
  """
  from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
  wordcloud = WordCloud(stopwords = STOPWORDS.add('s'),
                      collocations=True, width=1600, height=800,
                      max_words=20).generate(book)


  plt.figure(figsize=(20,10), facecolor='w')
  plt.imshow(wordcloud, interpolation='bilInear')
  plt.axis("off")
  plt.tight_layout(pad=0)
  plt.show()
