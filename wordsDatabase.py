import requests
import time

# open the file of words
wordsFile = open('words.txt','r')
words_definition = open('output.txt', 'a')
api_key = '186c73a1-3a44-4091-9e6d-a2cdf0d47608'
error = '\t Error: word was not found, check spelling\n'
torf = True

for word in wordsFile:
    # definition already exists
    arr = word.split('\t') 
    if len(arr) == 2:
        break

    response = requests.get(f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}')

    try:
        definition = str(response.json()[0].get('shortdef'))
    except:
        torf = False
        write_me = word[:-1] + '' + error

    if torf:
        # trim the [' and ']
        definition = definition[:-2]
        definition = definition[2:]
        definition = definition.replace('\'','')
        # write to a file, separate by a /t
        # remove the \n from the word
        write_me = word[:-1] + '\t' + definition + '\n' 
   
    words_definition.write(write_me)
    write_me = ''

print('Process completed.')