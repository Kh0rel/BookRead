import urllib.request
from tkinter import *
import requests
import xmltodict
from ToRead import ToRead
from Read import Read
from bs4 import BeautifulSoup

class SingleBook:

    def __init__(self, id):
        self.id = id
        self.url = 'https://www.goodreads.com/book/show/{}.xml?key=l1eCwD6ckPZinhRvhA9MSQ'.format(self.id)

    def getBook(self):
        request = requests.get(self.url)

        dict_book = xmltodict.parse(request.text)

        return dict_book

    def showBook(self, dict_book, frame):
        def add_to_read():
            add = ToRead()
            add.add(self.id)

        def add_read():
            read = Read()
            read.add(self.id)
        single = Tk()
        single['bg'] = 'white'

        book = dict_book['GoodreadsResponse']['book']
        frame_book = Frame(single, width=500, height=500)
        frame_book.pack()

        book_title = Label(frame_book, text=book['title'], font=("Helvetica bold", 14))
        book_title.pack()
        desc = BeautifulSoup(book['description'], "html.parser")
        book_desc = Text(frame_book)
        book_desc.pack()

        for line in desc:
            book_desc.insert(END, line.get_text())

        frame_button = Frame(frame_book, width=300, height=100)
        frame_button.pack(side=BOTTOM)

        Button(frame_button, text="Read", command=add_read).pack(side=LEFT, padx=10, pady=10)
        Button(frame_button, text="ToRead", command=add_to_read).pack(side=RIGHT, padx=10, pady=10)

        single.mainloop()
