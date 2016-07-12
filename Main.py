from tkinter import *
import Books


window = Tk()
window['bg']='white'

frameMenu = Frame(window, bg="gray", width=200, height=600)
frameMenu.pack(side=LEFT, fill=Y)

frameContent = Frame(window, bg="white", width=900, height=600)
frameContent.pack(side=RIGHT, fill=X)

frameLabelMenu = Frame(frameMenu, bg="darkgrey", highlightcolor="grey", width=200, height=100)
frameLabelMenu.pack(side=TOP)
labelTitle = Label(frameLabelMenu, text="BookRead", bg="darkgray").pack(padx=80, pady=20)


#Show Single Book Details
singleBookShow = Books.Books("TEST", "TEST", "TEST", frameContent)
singleBookShow.single_book()

# Show All Books

#allBooksShow = Books.Books("Test", "Toto", "Tata", frameContent)
#allBooksShow.show()

# Content Menu

frameBooks = Frame(frameMenu, bg="gray")
frameBooks.pack()
labelBooks = Label(frameBooks, text="Books", highlightcolor="darkgrey", bg="grey").pack(padx=10, pady=20)

frameRead = Frame(frameMenu, bg="gray")
frameRead.pack()
labelRead = Label(frameRead, text="Read", highlightcolor="darkgrey", bg="grey").pack(padx=10, pady=20)

frameToRead = Frame(frameMenu, bg="gray")
frameToRead.pack()
labelToRead = Label(frameToRead, text="To Read", highlightcolor="darkgrey", bg="grey").pack(padx=10, pady=20)

window.mainloop()
