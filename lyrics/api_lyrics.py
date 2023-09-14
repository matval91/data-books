# https://towardsdatascience.com/song-lyrics-genius-api-dcc2819c29
import lyricsgenius as lg

def get_song_lyrics(author_name='Aerosmith', song_title='Dream on'):
  """ Return song lyrics
  Function to obtain the lyrics of a song

  Args:
    author_name (str): the name of the author
    song_title  (str): the title of the song
    
  Returns:
    lyrics (str): the lyrics of the desired song
  """
  lyrics_raw=_get_raw_lyrics(author_name, song_title)
  lyrics = _clean_lyrics(lyrics_raw)
  return lyrics

def _get_raw_lyrics(author_name='Aerosmith', song_title='Dream on'):
  """ Return raw song lyrics
  Function to obtain the raw lyrics of a song

  Args:
    author_name (str): the name of the author
    song_title  (str): the title of the song
    
  Returns:
    lyrics (str): the lyrics of the desired song, not cleaned
  """
  import os
  # get the artist songs and the wanted song from genius
  token_lg = os.environ["LG_API_KEY"]
  genius = lg.Genius(token_lg)
  artist = genius.search_artist(author_name, max_songs=1)
  #artist = genius.search_artist(artist_name)
  song=artist.song(song_title)
  return song.lyrics

def _clean_lyrics(lyrics_raw):
  """ Return clean song lyrics
  Function to obtain the clean lyrics of a song

  Args:
    lyrics_raw (str): the raw lyrics
    
  Returns:
    lyrics (str): the lyrics of the desired song, without 
      comments or newlines
  """
  import re
  lyrics=lyrics_raw.split("Lyrics")[1]
  lyrics=lyrics.split('45')[0]
  lyrics=lyrics.replace('\n', ' ')

  # Define a regular expression pattern to match words between []
  pattern = r'\[([^\]]*)\]'    
  lyrics = re.sub(pattern, '', lyrics)
  pattern='[0-9]{2,4}Embed'
  lyrics = re.sub(pattern, '', lyrics)

  return lyrics