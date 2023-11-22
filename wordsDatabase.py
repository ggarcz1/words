import requests
import time
import socket
import sqlite3

# source for "test_network_connectivity()": https://chat.openai.com/share/abc86a1c-f1f8-4d0f-a9b0-26d7e571efbc
def test_network_connectivity(host, port):
    try:
        # Create a socket object
        sock = socket.create_connection((host, port), timeout=5)
        # print(f"Successfully connected to {host}:{port}")
        sock.close()
        return True
    except socket.error as e:
        print(f"Unable to connect to {host}:{port}. Error: {e}")
        return False

def get_definition(word):
    cursor.execute('SELECT * FROM words WHERE word=?', (word,))
    response = cursor.fetchall()
    sqliteConnection.close()
    return response

## this is the same as the code below
# def add_word(word):
#     if check_for_word(word=word):
#         return False
#     else:
#         sqliteConnection = sqlite3.connect('words.db')
#         cursor = sqliteConnection.cursor()
#         cursor.execute('SELECT * FROM words WHERE word=?', (word,))
#         values = [arr[0], arr[1]]
#         cursor.execute("INSERT INTO words VALUES (?, ?)",values)

#     return True

# True --> word exists in database
def check_for_word(word):
    sqliteConnection = sqlite3.connect('words.db')
    cursor = sqliteConnection.cursor()
    # check if user exists in the database already
    cursor.execute('SELECT * FROM words WHERE word=?', (word,))
    response = cursor.fetchall()
    sqliteConnection.close()
    return len(response) == 1


# open the file to add new words
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


for word in wordsFile:
    # check for if the definition already exists
    arr = word.split('\t')
    if len(arr) == 1 and not check_for_word(arr[0]):
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

        values = [word, write_me]
        sqliteConnection = sqlite3.connect('words.db')
        cursor = sqliteConnection.cursor()  
        cursor.execute("INSERT INTO words VALUES (?, ?)",values)
        # alphabetize
        cursor.execute("SELECT word,definition from words ORDER BY word ASC")
        sqliteConnection.commit()
        sqliteConnection.close()

        # words_definition.write(write_me)
        write_me = ''

if counter != 0:
    # write database to the output file 
    sqliteConnection = sqlite3.connect('words.db')
    cursor = sqliteConnection.cursor()  
    cursor.execute('SELECT * FROM words')
    response = cursor.fetchall()
    
    sqliteConnection.close()
    sqliteConnection.close()
 
print('Process completed. ' + str(counter) + ' words have been searched.')
