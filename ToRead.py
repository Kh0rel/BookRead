import urllib.request
from tkinter import *
import requests
import xmltodict


class ToRead:
    def __init__(self):
        self.api_key = 'l1eCwD6ckPZinhRvhA9MSQ'
        self.url = 'https://www.goodreads.com/review/list/46998003.xml?key={}&v=2&shelf=to-read'.format(self.api_key)

    def get(self):
        request = requests.get(self.url)

        dict_to_read = xmltodict.parse(request.text)

        return dict_to_read

    def add(self, id):
        url = 'https://www.goodreads.com/shelf/add_to_shelf.xml?name=to-read&book_id={}'.format(id)
        requests.post(url)

    def remove(self,id):
        url='https://www.goodreads.com/shelf/add_to_shelf.xml?name=to-red&book_id={}?a=remove'.format(id)
        requests.post(url)

    def show(self,dict_to_read, frame):
        i = 0
        frame_book_left = Frame(frame, width=100, height=200)
        frame_book_left.pack(side=LEFT)
        frame_book_right = Frame(frame, width=100, height=200)
        frame_book_right.pack(side=RIGHT)
        for book in dict_to_read['GoodreadsResponse']['reviews']['review']:
            if i <= 10:
                single_book_left = Frame(frame_book_left)
                single_book_left.pack(padx=10, pady=10)
                book_title_left = Label(single_book_left, text=book['book']['title'], font=("Helvetica bold", 14))
                book_author_left = Label(single_book_left, text=book['book']['authors']['author']['name'])

                book_title_left.pack()
                book_author_left.pack()
            else:
                single_book_right = Frame(frame_book_right)
                single_book_right.pack(padx=10, pady=10)
                book_title_right = Label(single_book_right, text=book['book']['title'], font=("Helvetica bold", 14))
                book_author_right = Label(single_book_right, text=book['book']['authors']['author']['name'])

                book_title_right.pack()
                book_author_right.pack()
            i += 1