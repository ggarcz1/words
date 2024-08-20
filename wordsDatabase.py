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
    return len(response) >= 1

wordsFileName = 'words.txt'
# open the file to add new words
wordsFile = open(f'{wordsFileName}','r')
# words_definition = open('words.txt', 'a')
api_key = '186c73a1-3a44-4091-9e6d-a2cdf0d47608'
error = '\t Error: word was not found, check spelling\n'
write_me = ''
counter = counter_phrases = 0
host_to_test = "google.com"
port_to_test = 443
duplicates = []
word_flag = True

# test for network connectivity here
if not test_network_connectivity(host_to_test, port_to_test):
    print(f'Error.  No connectivity to {host_to_test}')
    exit(0)

print(f'Searching for the words in the file "{wordsFileName}"...')

write_me = definition = None

for word in wordsFile:
    print(word)
    word = word.lower()
    if ' ' in word:
        word_flag = False

    # check for if the definition already exists
    arr = word.split('\t')
    if check_for_word(arr[0]):
        duplicates.append(arr[0])
    else:
        arr = word.split(' ')
        if len(arr) == 1:
            response = requests.get(f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}')
        # word was added
            try:
                    definition = str(response.json()[0].get('shortdef'))
                    # trim the [' and ']
                    definition = definition[:-2]
                    definition = definition[2:]
                    definition = definition.replace('\'','')
                    # write to a file, separate by a /t
                    # remove the \n from the word
                    counter += 1
            except:
                definition = error

            values = [word, definition]

        # phrase present 
        elif len(arr) > 1:
            word_flag = False
            counter_phrases += 1
            values = word


        db = 'words.db'

        if word_flag == False:
            sqliteConnection = sqlite3.connect(f'{db}')
            cursor = sqliteConnection.cursor()  
            cursor.execute("INSERT INTO phrases VALUES (?)",[values])
        
        else:
            sqliteConnection = sqlite3.connect(f'{db}')
            cursor = sqliteConnection.cursor()  
            cursor.execute("INSERT INTO words VALUES (?, ?)",values)
            
        sqliteConnection.commit()


        
# alphabetize
# cursor.execute("SELECT word,definition from words ORDER BY word ASC")
# sqliteConnection.commit()
# sqliteConnection.close()

# overwrite the initial input file 
# wordsFile = open('words.txt','w')
# wordsFile.write('')
# wordsFile.close()

# fetch all from database post write
# sqliteConnection = sqlite3.connect('words.db')
# cursor = sqliteConnection.cursor()  
# cursor.execute('SELECT * FROM words')
# response = cursor.fetchall()
# for each in response:
#     print(each)
        
print('Process completed. ' + str(counter) + ' words have been searched.')
print('Process completed. ' + str(counter_phrases) + ' phrases have been added.')

if len(duplicates) != 0:
    print('The following duplicates were discovered: ')
    print(duplicates)
