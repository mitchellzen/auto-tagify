import re
import urllib
import nltk
from nltk.stem.wordnet import WordNetLemmatizer

class AutoTagify():
  clean_word = re.compile('[\[\],().:;"\/\'?*%!*+=@$;#%{}`~\r\n\t]')
  smart_quotes_s = re.compile('(\xe2\x80\x98)|(\xe2\x80\x99)|(\&#8216;)|(\&#8217;)')
  smart_quotes_d = re.compile('(\xe2\x80\x9c)|(\xe2\x80\x9d)|(\&#8220;)|(\&#8221;)')
  long_dash = re.compile('(\&#8212;)')
  clean_link = re.compile('(?<=^\/)\/+|\/+$')
  link_pattern_a = re.compile(r"(^|[\n ])(([\w]+?://[\w\#$%&~.\-;:=,?@\[\]+]*)(/[\w\#$%&~/.\-;:=,?@\[\]+]*)?)", re.IGNORECASE | re.DOTALL)
  link_pattern_b = re.compile(r"#(^|[\n ])(((www|ftp)\.[\w\#$%&~.\-;:=,?@\[\]+]*)(/[\w\#$%&~/.\-;:=,?@\[\]+]*)?)", re.IGNORECASE | re.DOTALL)

  stop_words = ['DT', 'IN', 'TO', 'VBD', 'VBD', 'VBG', 'VBN', 'VBZ', 'MD', 'RB', 'CC', 'WDT']
  min_tag_length = 2
  lemma = WordNetLemmatizer()
  
  def __init__(self):
    self.css = ''
    self.link = ''
    self.text = ''
    
  def generate(self,strict=True,html=True):
    tag_words = ''
    for (word, word_type) in self.__tokenize():
      print word
      tag_word = self.__cleaned(word,strict)
      if len(tag_word) > self.min_tag_length and word_type not in self.stop_words:
        if html and self.__is_hyperlink(word):
          tag_words += '<a href="'+word+'" target="_blank">'+word+'</a>'
        else:
          tag_words += '<a href="'+self.clean_link.sub('', self.link)+'/'+urllib.quote(tag_word)+'" class="'+self.clean_word.sub('',self.css)+'">'+self.__replace_special_chars(word)+'</a> '
      else:
        tag_words += word+' '
    return tag_words
  
  def tag_list(self,strict=True):
    tag_words = []
    for (word, word_type) in self.__tokenize():
      tag_word = self.__cleaned(word,strict)
      if len(tag_word) > self.min_tag_length and word_type not in self.stop_words: tag_words.append(tag_word)
    return tag_words
  
  def __is_hyperlink(self,word):
    if self.link_pattern_a.match(word) or self.link_pattern_b.match(word):
      return True
    else:
      return False
    
  def __tokenize(self,html=True):
    if html and self.__is_hyperlink(self.text):
      return [(self.text, '')]
    else:
      return nltk.pos_tag(nltk.word_tokenize(self.__clean_text()))
    
  def __cleaned(self,word,strict):
    lemmatized = self.lemma.lemmatize(self.__clean_text(word))
    if strict:
      return lemmatized
    else:
      return urllib.quote(lemmatized)
      
  def __clean_text(self,word=''):
    if len(word) > self.min_tag_length:
      return self.clean_word.sub('',self.__replace_special_chars(word.lower()))
    else:
      return self.clean_word.sub('',self.__replace_special_chars(self.text))
      
  def __replace_special_chars(self, text):
    return self.smart_quotes_s.sub('\'',self.smart_quotes_d.sub('"',self.long_dash.sub('-',text)))