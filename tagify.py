import re

def tagify(text):
  return remove_stop_words(remove_ctrl_chars(text).split(' '))
  
def clean_word(word):
  return re.compile('[,().;:"\'?!*&<>/\+={}`~]').sub('', word)
  
def remove_ctrl_chars(text):
  return re.compile('[\r\n\t]').sub(' ', text)

def remove_stop_words(text):
  tag_words = []
  for word in text:
    word = clean_word(word)
    if len(word) > 2 and not bool(re.match('(^(th|wh|hi|sh|an|ha|wa)[adeisouy]$)|(^(th|wh|do|is|he)[aeionur][nste]$)|(^(wh|th|h|w)(ere))|(^(w|sh|c)(ould))|(but)|(how)|(very)|(really)', word, re.IGNORECASE)):
      tag_words.append(word)
        
  return sorted(tag_words)
  