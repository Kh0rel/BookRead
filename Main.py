from tkinter import *
from Books import AllBooks
from Book import SingleBook
from ToRead import ToRead
from Read import Read



window = Tk()
window['bg'] = 'white'

frameMenu = Canvas(window, bg="gray", width=200, height=600)
frameMenu.pack(side=LEFT, fill=Y)


def content():
    content.frameContent = Canvas(window, bg="white", width=900, height=600)
    content.frameContent.pack(side=RIGHT, fill=X)

content()

frameLabelMenu = Frame(frameMenu, bg="darkgrey", highlightcolor="grey", width=200, height=100)
frameLabelMenu.pack(side=TOP)
labelTitle = Label(frameLabelMenu, text="BookRead", bg="darkgray").pack(padx=80, pady=20)


def show_books():
    content.frameContent.pack_forget()
    content()
    Books = AllBooks()
    dict_books = Books.getBooks()
    Books.showBooks(dict_books, content.frameContent)


def show_to_read():
    content.frameContent.pack_forget()
    content()
    toRead = ToRead()
    dict_to_read = toRead.get()
    toRead.show(dict_to_read, content.frameContent)


def show_read():
    content.frameContent.pack_forget()
    content()
    read = Read()
    dict_read = read.get()
    read.show(dict_read, content.frameContent)


# Content Menu

buttonBooks = Button(frameMenu, text="Books", bg="grey", command=show_books)
buttonBooks.pack()
buttonToRead = Button(frameMenu, text="To Read", bg="grey", command=show_to_read)
buttonToRead.pack()
buttonRead = Button(frameMenu, text="Read", bg="grey", command=show_read)
buttonRead.pack()


window.mainloop()
