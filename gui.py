import sqlite3
import tkinter as tk
from tkinter import ttk


# source, for now
# https://www.pythontutorial.net/tkinter/tkinter-scrollbar/

root = tk.Tk()
root.resizable(False, False)
root.title("Scrollbar Widget Example")

# apply the grid layout
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# create the text widget
text = tk.Text(root, height=35, width=200)
text.grid(row=0, column=0, sticky=tk.EW)

scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
scrollbar.grid(row=0, column=1, sticky=tk.NS)

text['yscrollcommand'] = scrollbar.set

conn = sqlite3.connect('words.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM words")
data = cursor.fetchall()

counter = 1
for i in data:
    position = f'{counter}.0'
#     i = i.split(',')
    text.insert(position, str(i[0].upper())+'\t'+str(i[1])+'\n')
    counter += 1

root.mainloop()


# add buttons to add a word
# add button to search
# add button to 