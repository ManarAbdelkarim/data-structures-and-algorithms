import re
class HashMap:
  def __init__(self, size=1024):
    self.size = size
    self.buckets = [None]*size

  def hash(self,key):
    '''
    this function takes a string value and return hashed key
    '''
    sum = 0
    for letter in key:
       sum= (sum + ord(letter)* key.index(letter) * 19)% self.size
    return  sum

  def add(self,key):
    '''
    this function take a string key and a value then add them in the hashtable as a list
    '''
    index = self.hash(key)
    if self.buckets[index] is None:
      self.buckets[index] = key
      return None
    return key

  def first_repeated(self , string):
    if string == '':
        raise Exception("the string is empty")
    string = re.sub(r'[^\w\s]', '', string)
    strings = string.split(' ')
    for word in strings:
      if self.add(word):
        return word
    return 'No repeated words'


hashm = HashMap()
# hashm.collision("hello world everyone, hello")

print(hashm.first_repeated("Once upon a time, there was a brave princess who..."))
