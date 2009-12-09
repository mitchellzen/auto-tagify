import re
import urllib
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

class AutoTagify():
  clean_word = re.compile('[\[\],().:;|"\'?!*<>/\+={}@#^&`~\s]')
  smart_quotes_s = re.compile('(\xe2\x80\x98)|(\xe2\x80\x99)')
  smart_quotes_d = re.compile('(\xe2\x80\x9c)|(\xe2\x80\x9d)')
  clean_link = re.compile('(?<=^\/)\/+|\/+$')
  stop_words = ['DT', 'IN', 'TO', 'VBD', 'VBD', 'VBG', 'VBN', 'VBZ', 'MD', 'RB']
  min_tag_length = 2
  lemma = WordNetLemmatizer()
  stem = PorterStemmer()
  
  def __init__(self):
    self.css = ''
    self.link = ''
    self.text = ''
    
  def generate(self,strict=True):
    tag_words = ''
    for (word, word_type) in self.__tokenize():
      tag_word = self.__cleaned(word,strict)
      if len(tag_word) > self.min_tag_length and word_type not in self.stop_words:
        tag_words += '<a href="'+self.clean_link.sub('', self.link)+'/'+urllib.quote(tag_word)+'" class="'+self.clean_word.sub('',self.css)+'">'+word+'</a> '
      else:
        tag_words += word+' '
    return tag_words
  
  def tag_list(self,strict=True):
    tag_words = []
    for (word, word_type) in self.__tokenize():
      tag_word = self.__cleaned(word,strict)
      if len(tag_word) > self.min_tag_length and word_type not in self.stop_words: tag_words.append(tag_word)
    return tag_words
    
  def __tokenize(self):
    return nltk.pos_tag(nltk.word_tokenize(self.text))
    
  def __cleaned(self,word,strict):
    lemmatized = self.stem.stem(self.lemma.lemmatize(self.clean_word.sub('',self.smart_quotes_s.sub('\'',self.smart_quotes_d.sub('"',word.lower())))))
    if strict:
      return lemmatized
    else:
      return urllib.quote(lemmatized)