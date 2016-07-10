from tkinter import *
import Books

window = Tk()
window['bg']='white'

FrameMenu = Frame(window, bg="gray", width=200, height=600)
FrameMenu.pack(side=LEFT, fill=Y)

FrameContent = Frame(window, bg="white", width=900, height=600)
FrameContent.pack(side=RIGHT, fill=X)

FrameLabelMenu = Frame(FrameMenu, bg="darkgrey", highlightcolor="grey", width=200, height=100)
FrameLabelMenu.pack(side=TOP)
LabelTitle = Label(FrameLabelMenu, text="BookRead", bg="darkgray").pack(padx=80, pady=20)


#Show Single Book Details
#singleBookShow = Books.Books("TEST", "TEST", "TEST", FrameContent)
#singleBookShow.single_book()

# Show All Books

#allBooksShow = Books.Books("Test", "Toto", "Tata", FrameContent)
#allBooksShow.show_book()

# Content Menu

FrameBooks = Frame(FrameMenu, bg="gray")
FrameBooks.pack()
LabelBooks = Label(FrameBooks, text="Books", highlightcolor="darkgrey", bg="grey").pack(padx=10, pady=20)

FrameRead = Frame(FrameMenu, bg="gray")
FrameRead.pack()
LabelRead = Label(FrameRead, text="Read", highlightcolor="darkgrey", bg="grey").pack(padx=10, pady=20)

FrameToRead = Frame(FrameMenu, bg="gray")
FrameToRead.pack()
LabelToRead = Label(FrameToRead, text="To Read", highlightcolor="darkgrey", bg="grey").pack(padx=10, pady=20)

window.mainloop()