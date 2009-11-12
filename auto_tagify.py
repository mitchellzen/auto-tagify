import re

class auto_tagify():
  stop_word = re.compile('(^(th|wh|hi|sh|an|ha|wa)[adeisouy]$)|(^(th|wh|do|is|he)[aeionur][nste]$)|(^(wh|th|h|w)(ere))|(^(w|sh|c)(ould))|(but)|(how)|(very)|(really)')
  eol = re.compile('[\r\n\t]')
  clean_word = re.compile('[\[\],().;:"\'?!*&<>/\+={}`~]')
  clean_link = re.compile('(?<=^\/)\/+|\/+$')
  min_length = 2
  
  def __init__(self):
    self.css_class = ''
    self.link_path = ''
    self.text = ''
    
  def generate(self):
    tag_words = ''

    for word in self.eol.sub(' ',self.text).split(' '):
      tag_word = self.clean_word.sub('',word).lower()
      if len(tag_word) > self.min_length and not self.stop_word.match(tag_word):
        tag_words += '<a href="'+self.clean_link.sub('', self.link_path)+'/'+tag_word+'" class="'+self.clean_word.sub('',self.css_class)+'">'+word+'</a> '
      else:
        tag_words += word+' '

    return tag_words
  
  def tag_list(self):
    tag_words = []

    for word in self.eol.sub(' ',self.text).split(' '):
      tag_word = self.clean_word.sub('',word).lower()
      if len(tag_word) > self.min_length and not self.stop_word.match(word):
        tag_words.append(tag_word)
 
    return tag_words