import sqlite3

sqliteConnection = sqlite3.connect('words.db')
cursor = sqliteConnection.cursor()
# cursor.execute("CREATE TABLE words(word, definition)")

# cursor.execute("DELETE FROM words WHERE word=?",('test',))
# wordsFile = open('words.txt','r')

# for word in wordsFile:
#     arr = word.split('\t')
#     if len(arr) == 2:
#         values = [arr[0], arr[1]]
#         cursor.execute("INSERT INTO words VALUES (?, ?)",values)
    
cursor.execute("SELECT COUNT(*) FROM words")
print(cursor.fetchall())

word = 'volupdstuously'
cursor.execute("SELECT * FROM words WHERE word=?",(word,))
print(len((cursor.fetchall())))

sqliteConnection.commit()
sqliteConnection.close()

