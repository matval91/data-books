#https://github.com/raduangelescu/gutenbergpy

import gutenbergpy.textget
import chardet

def get_book(id=2701):
  """
  Function to retrieve a book 
  """
  # This book should be Moby Dick
  raw_book = gutenbergpy.textget.get_text_by_id(id) # with headers
  clean_book = gutenbergpy.textget.strip_headers(raw_book) # without headers

  # determine encoding of clean_book
  the_encoding = chardet.detect(clean_book)['encoding']
  if the_encoding !='utf-8':
    print(f'The encoding is {the_encoding} and not utf-8 \n')
  
  return str(clean_book, the_encoding)


def cache():
  """
  How to create the new cache

  from gutenbergpy.gutenbergcache import GutenbergCache
  GutenbergCache.create(refresh=True, download=True, unpack=True, parse=True, 
    cache=True, deleteTemp=True)
  cache = GutenbergCache.get_cache()
  """
  from gutenbergpy.gutenbergcache import GutenbergCache
  cache = GutenbergCache.get_cache()
  cursor = cache.native_query("SELECT * FROM authors")
  ee=cursor.fetchall()
  # for x in ee: print(x)

def cache_author_id_from_name(name='Koch, Ernst'):
  """
  """
  from gutenbergpy.gutenbergcache import GutenbergCache
  cache = GutenbergCache.get_cache()
  cursor = cache.native_query(f"SELECT ID FROM authors WHERE name={name}")
  author_id=cursor.fetchall()
  author_id=author_id[0][0]
  print(f"The ID for author {name} is {author_id}")
  return author_id

def cache_book_id_from_title(title='Moby Dick'):
  """
  """
  from gutenbergpy.gutenbergcache import GutenbergCache
  cache = GutenbergCache.get_cache()
  cursor = cache.native_query(f"SELECT id FROM titles WHERE name=\'{title}\'")
  book_id=cursor.fetchall()
  book_id = book_id[0][0]
  print(f"The ID for book {title} is {book_id}")

  cursor = cache.native_query(f"SELECT * from books WHERE id=\'{book_id}\'")
  book_id=cursor.fetchall()

  return book_id
