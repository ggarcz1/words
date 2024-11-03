import sqlite3

sqliteConnection = sqlite3.connect('words.db')
cursor = sqliteConnection.cursor()
query = 'SELECT * FROM words'
cursor.execute(query)
response = cursor.fetchall()
sqliteConnection.close()

f_words_def = open('all_defs.txt', 'w')
f_just_words = open('all_words.txt','w')

for each in response:
    # [:-1] will get rid of the \n after each word
    string = f'{each[0][:-1]}\t{each[1]}'
    f_words_def.write(f'{string}\n')
    f_just_words.write(f'{each[0][:-1]}\n')

print('Done.')