import re

class Tagify():
  def __init__(self,text,link_path=''):
    text = re.compile('[\r\n\t]').sub(' ',text).split(' ')
    self._get_tagged(text,link_path)

  def _get_tagged(self,text,link_path):
    tag_words = ''
    stop_word = re.compile('(^(th|wh|hi|sh|an|ha|wa)[adeisouy]$)|(^(th|wh|do|is|he)[aeionur][nste]$)|(^(wh|th|h|w)(ere))|(^(w|sh|c)(ould))|(but)|(how)|(very)|(really)')
  
    clean_word = re.compile('[\[\],().;:"\'?!*&<>/\+={}`~]')
    link_path = re.compile('(\/)$').sub('',link_path)
  
    for word in text:
      tag_word = clean_word.sub('',word).lower()
    
      if len(word) > 2 and not bool(stop_word.match(word,re.IGNORECASE)):
        tag_words += '<a href="'+link_path+'/'+tag_word+'">'+word+'</a> '
      else:
        tag_words += word+' '
        
    print tag_words