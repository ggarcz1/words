import sqlite3
import sys

def search_database(search_string, flag):
    sqliteConnection = sqlite3.connect('words.db')
    cursor = sqliteConnection.cursor()

    if len(search_string) <= 0:
        return 'No search parameter specified.'
    
    if flag == 1:
        query = 'SELECT * FROM words WHERE word LIKE ?'
        cursor.execute(query, ('%' + search_string + '%',))
    elif flag == 2:
        query = 'SELECT * FROM words WHERE definition LIKE ?'
        cursor.execute(query, ('%' + search_string + '%',))
    else:
        return 'Invalid Flag.  1 for word search 2 for definition search'
    
    response = cursor.fetchall()
    sqliteConnection.close()
    return response


if len(sys.argv) == 1:
    flag = input('Enter 1 for word and 2 for definiton search: ')
    search = input('Enter search parameter: ')
    values = search_database(search, int(flag))
else:
    values = search_database(search_string=sys.argv[1], flag=sys.argv[2])


if values == 'Invalid Flag.  1 for word search 2 for definition search':
    print(values)
    exit()

# print(values)
for each in values:
    print(f'{each[0]}: {each[1]}')