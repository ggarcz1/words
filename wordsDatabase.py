import requests
import time
import socket

# source for "test_network_connectivity(_,_)": https://chat.openai.com/share/abc86a1c-f1f8-4d0f-a9b0-26d7e571efbc
def test_network_connectivity(host, port):
    try:
        # Create a socket object
        sock = socket.create_connection((host, port), timeout=5)
        print(f"Successfully connected to {host}:{port}")
        sock.close()
        return True
    except socket.error as e:
        print(f"Unable to connect to {host}:{port}. Error: {e}")
        return False



def search(fileObject,word):
    for idx in fileObject:
        line = idx.split('\t')
        # assuming a-z
        # word will pass where it should be alphabetically
        if line[0] > word and line[0] != word:
            return False
        if word == line[0]:
            return True
    
    return False

# open the file of words
wordsFile = open('words.txt','r')
words_definition = open('words.txt', 'a')
api_key = '186c73a1-3a44-4091-9e6d-a2cdf0d47608'
error = '\t Error: word was not found, check spelling\n'
write_me = ''
counter = 0
host_to_test = "google.com"
port_to_test = 443

# test for network connectivity here
if not test_network_connectivity(host_to_test, port_to_test):
    exit(0)

# works
# print(search(wordsFile,'acid'))

for word in wordsFile:
    # check for if the definition already exists
    arr = word.split('\t')
    if len(arr) == 1 and search(wordsFile,arr[0]):
        response = requests.get(f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}')

        try:
            definition = str(response.json()[0].get('shortdef'))
            # trim the [' and ']
            definition = definition[:-2]
            definition = definition[2:]
            definition = definition.replace('\'','')
            # write to a file, separate by a /t
            # remove the \n from the word
            write_me = word[:-1] + '\t' + definition + '\n' 
            counter += 1
        except:
            write_me = word[:-1] + '' + error

        words_definition.write(write_me)
        write_me = ''

print('Process completed. ' + str(counter) + ' words have been searched.')
