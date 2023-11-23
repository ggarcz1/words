import sqlite3
import sys

def search_database(search_string):
    sqliteConnection = sqlite3.connect('words.db')
    cursor = sqliteConnection.cursor()
    # check if user exists in the database already
    query = 'SELECT * FROM words WHERE definition LIKE ?'
    cursor.execute(query, ('%' + search_string + '%',))
    response = cursor.fetchall()
    sqliteConnection.close()
    return response


if len(sys.argv) == 1:
    values = search_database(input('Enter data: '))
else:
    values = search_database(sys.argv[1])


for each in values:
    print(each)