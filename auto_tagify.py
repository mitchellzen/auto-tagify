import re

class AutoTagify():
  stop_word = re.compile('(^(th|wh|hi|sh|an|ha|wa)[adeisouy]$)|(^(th|wh|do|is|he)[aeionur][nste]$)|(^(wh|th|h|w)(ere))|(^(w|sh|c)(ould))|(but)|(how)|(very)|(really)|(with)')
  eol = re.compile('[\r\n\t]')
  clean_word = re.compile('[\[\],().;:"\'?!*&<>/\+={}`~]')
  clean_link = re.compile('(?<=^\/)\/+|\/+$')
  min_word_length = 3
  
  def __init__(self):
    self.css = ''
    self.link = ''
    self.text = ''
    
  def generate(self):
    tag_words = ''

    for word in self.eol.sub(' ',self.text).split(' '):
      tag_word = self.clean_word.sub('',word).lower()
      if len(tag_word) >= self.min_word_length and not self.stop_word.match(tag_word):
        tag_words += '<a href="'+self.clean_link.sub('', self.link)+'/'+tag_word+'" class="'+self.clean_word.sub('',self.css)+'">'+word+'</a> '
      else:
        tag_words += word+' '

    return tag_words
  
  def tag_list(self):
    tag_words = []

    for word in self.eol.sub(' ',self.text).split(' '):
      tag_word = self.clean_word.sub('',word).lower()
      if len(tag_word) >= self.min_word_length and not self.stop_word.match(tag_word):
        tag_words.append(tag_word)
 
    return tag_words