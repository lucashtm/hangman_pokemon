import requests
import random
import json

url = 'http://pokeapi.co/api/v2/pokemon/'
number = random.randint(1, 151)
url = url+str(number)

r = requests.get(url)
body = r.content.decode('utf-8')
pokemon = json.loads(body)

hang = { 'word': pokemon['name'], 'mask': '_ '*len(pokemon['name']) }
tries = 0

def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

while '_' in hang['mask'] and tries < 10:
  print(hang['mask'])
  print(tries)
  word_letter = input('>')
  tries += 1
  if word_letter == hang['word']:
    for i in range(len(hang['word'])):
      hang['mask'] = replace_str_index(hang['mask'], i*2, hang['word'][i])
    break
  elif len(word_letter) > 1:
    print('Wrong!')
  else:
    for i in range(len(hang['word'])):
      if hang['word'][i] == word_letter:
          hang['mask'] = replace_str_index(hang['mask'], i*2, word_letter)

print(hang['mask'])
if '_' in hang['mask']:
  print('You lost!')
  print('Answer: ', hang['word'])
else:
  print('Correct!')