import requests

# open the file of words
wordsFile = open('words.txt')

# for word in wordsFile:
#   response = requests.get('https://www.dictionary.com/browse/'+word)


# https://dictionaryapi.com/products/api-collegiate-dictionary

word = 'special'
api_key = ''
response = requests.get(f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}')
response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/'+word).json()
# print(response)
print(response)



# value = 'aboriginal	Having existed in a region from the beginning'
# print(value.split('\t'))


