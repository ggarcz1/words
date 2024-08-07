import sqlite3

sqliteConnection = sqlite3.connect('words.db')
cursor = sqliteConnection.cursor()
# cursor.execute('CREATE TABLE words(word, definition)')
# cursor.execute('CREATE TABLE phrases(phrase)')

# cursor.execute('DROP TABLE words')
# cursor.execute('DELETE FROM words WHERE word=?',('test',))


## add to the db from a file of word:definition
# for word in wordsFile:
#     arr = word.split('\t')
#     if len(arr) == 2:
#         values = [arr[0], arr[1]]
#         cursor.execute('INSERT INTO words VALUES (?, ?)',values)
    
cursor.execute('SELECT COUNT(*) FROM words')
count = (str(cursor.fetchall()[0])[:-2])[1:]
print(f'There are {count} entries in the Words Database')

cursor.execute('SELECT COUNT(*) FROM phrases')
count = (str(cursor.fetchall()[0])[:-2])[1:]
print(f'There are {count} entries in the Phrases Database')

# cursor.execute('SELECT * FROM words')
# print(cursor.fetchall())

cursor.execute('SELECT * FROM phrases')
print(cursor.fetchall())

# word = 'volupdstuously'
# cursor.execute('SELECT * FROM words WHERE word=?',(word,))
# # print(len((cursor.fetchall())))

# word = 'aberrants'
# cursor.execute('SELECT definition FROM words WHERE word=?',(word,))
# print(cursor.fetchall()[0])

sqliteConnection.commit()
sqliteConnection.close()

