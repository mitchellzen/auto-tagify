import re

class auto_tagify():
  def __init__(self,text='',link_path='',tags_only=False):
    text = re.compile('[\r\n\t]').sub(' ',text).split(' ')
    
    stop_word = re.compile('(^(th|wh|hi|sh|an|ha|wa)[adeisouy]$)|(^(th|wh|do|is|he)[aeionur][nste]$)|(^(wh|th|h|w)(ere))|(^(w|sh|c)(ould))|(but)|(how)|(very)|(really)')
    
    clean_word = re.compile('[\[\],().;:"\'?!*&<>/\+={}`~]')
    
    if tags_only:
      self.__get_tag_list(text,stop_word,clean_word)
    else:
      self.__get_tagged_result(text,link_path,stop_word,clean_word)
    
  def __get_tagged_result(self,text,link_path,stop_word,clean_word):
    tag_words = ''
    link_path = re.compile('(\/+)$').sub('',link_path)
  
    for word in text:
      tag_word = clean_word.sub('',word).lower()
    
      if len(tag_word) > 2 and not stop_word.match(tag_word):
        tag_words += '<a href="'+link_path+'/'+tag_word+'">'+word+'</a> '
      else:
        tag_words += word+' '
        
    return tag_words
  
  def __get_tag_list(self,text,stop_word,clean_word):
    tag_words = []
    tag_count_list = {}
    
    for word in text:
      tag_word = clean_word.sub('',word).lower()
      
      if len(tag_word) > 2 and not stop_word.match(word):
        tag_words.append(tag_word)
 
    return tag_words