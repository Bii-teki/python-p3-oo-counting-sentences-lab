#!/usr/bin/env python3
import re
class MyString:
  def __init__(self, value=' '):
    self.value = value

  def get_value(self): 
    return self._value

  def set_value(self, value):
    if type(value) is str:
      self._value=value 
    else:
      print("The value must be a string.") 

  value=property(get_value, set_value)

  def is_sentence(self):
    return self._value.endswith(".") 
  
  def is_question(self):
    return self._value.endswith("?") 
  
  def is_exclamation(self):
    return self._value.endswith("!") 
  
  def count_sentences(self):
    value = self.value
    value = re.sub(r'[!?\n]', '.', value)
    sentences = re.split(r'[.]+|[;]+|[:]+|\n+', value)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    return len(sentences)


       
    





