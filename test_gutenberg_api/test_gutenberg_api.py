#https://github.com/raduangelescu/gutenbergpy

import gutenbergpy.textget
import chardet

# This book should be Moby Dick
raw_book = gutenbergpy.textget.get_text_by_id(2701) # with headers
clean_book = gutenbergpy.textget.strip_headers(raw_book) # without headers


# determine encoding of clean_book
the_encoding = chardet.detect(clean_book)['encoding']
if the_encoding !='utf-8':
  print(f'The encoding is {the_encoding} and not utf-8 \n')

aa=str(clean_book, 'UTF-8')
