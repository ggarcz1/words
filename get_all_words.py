import sqlite3

sqliteConnection = sqlite3.connect('words.db')
cursor = sqliteConnection.cursor()
query = 'SELECT * FROM words'
cursor.execute(query)
response = cursor.fetchall()
sqliteConnection.close()

# f = open('all_words.txt','w')
# print(values)
for each in response:
    print(f'{each[0]}\n')
    # f.write(f'{each[0]}\n')

# print('Done. Removing \n')





