import requests
import time
import json

# open the file of words
wordsFile = open('words.txt','r')
words_definition = open('output.txt', 'w')
api_key = '186c73a1-3a44-4091-9e6d-a2cdf0d47608'

for word in wordsFile:
    response = requests.get(f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}')
    # time.sleep(1)
    definition = str(response.json()[0].get('shortdef'))
    # trim the [' and ']
    definition = definition[:-2]
    definition = definition[2:]
    definition = definition.replace('\'','')
    # write to a file, separate by a /t
    write_me = word[:-1] + '\t' + definition + '\n'
    # write_me = '\''+word+'\''+':'+'\''+definition+'\','
    words_definition.write(write_me)


# value = 'aboriginal	Having existed in a region from the beginning'
# print(value.split('\t'))


