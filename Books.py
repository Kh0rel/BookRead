import urllib.request
from tkinter import *
import io
from PIL import Image, ImageTk

class Books:
    def __init__(self, title, desc, img, frame):
        self.title = title
        self.desc = desc
        self.img = img
        self.frame = frame

    def show(self):
        frameBook = Frame(self.frame, width=100, height=200)
        frameBook.pack()

        fd = urllib.request.urlopen("https://d.gr-assets.com/books/1444087507m/26847020.jpg")
        imgFile = io.BytesIO(fd.read())
        im = ImageTk.PhotoImage(Image.open(imgFile))
        image = Label(frameBook, image=im)
        image.grid(row=2, column=0)
        cover = Canvas(frameBook, width=50, height=100)
        cover.pack()

        bookTitle = Label(frameBook, text=self.title)
        bookTitle.pack()

    def single_book(self):
        frameSingleBook = Frame(self.frame, width=500, height=500)
        frameSingleBook.pack()
        fd = urllib.request.urlopen("https://d.gr-assets.com/books/1444087507m/26847020.jpg")
        imgFile = io.BytesIO(fd.read())
        im = ImageTk.PhotoImage(Image.open(imgFile))
        image = Label(frameSingleBook, image=im)
        image.grid(row=2, column=0)
        coverSingle = Canvas(frameSingleBook, width=100, height=250)
        coverSingle.pack(side=RIGHT)

        bookSingleTitle = Label(frameSingleBook, text=self.title)
        bookSingleTitle.pack(side=LEFT)

        bookSingleDesc = Label(frameSingleBook, text= self.desc)
        bookSingleDesc.pack()

        frameButton = Frame(frameSingleBook, width=300, height= 100)
        frameButton.pack(side=BOTTOM)

        buttonRead = Button(frameButton, text="Read").pack(side=LEFT, padx=10, pady=10)
        buttonToRead = Button(frameButton, text="ToRead").pack(side=RIGHT, padx=10, pady=10)
