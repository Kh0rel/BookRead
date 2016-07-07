from tkinter import *
import string

fenetre = Tk()

#Label de base

label1 = Label(fenetre, text="Hello World")
label1.pack()

#Boutton

boutonTest=Button(fenetre, text="Fermer", command=fenetre.quit)
boutonTest.pack()

#Label background color
label2 = Label(fenetre, text="Texte par défaut", bg="yellow")
label2.pack()

#Input

value = StringVar()
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=string, width=30)
entree.pack()

# checkbutton
bouton = Checkbutton(fenetre, text="Nouveau?")
bouton.pack()

# radiobutton
value = StringVar()
bouton1 = Radiobutton(fenetre, text="Oui", variable=value, value=1)
bouton2 = Radiobutton(fenetre, text="Non", variable=value, value=2)
bouton3 = Radiobutton(fenetre, text="Peu être", variable=value, value=3)
bouton1.pack()
bouton2.pack()
bouton3.pack()

# liste
liste = Listbox(fenetre)
liste.insert(1, "Python")
liste.insert(2, "PHP")
liste.insert(3, "jQuery")
liste.insert(4, "CSS")
liste.insert(5, "Javascript")

liste.pack()

# canvas
canvas = Canvas(fenetre, width=150, height=120, background='yellow')
ligne1 = canvas.create_line(75, 0, 75, 120)
ligne2 = canvas.create_line(0, 60, 150, 60)
txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="blue")
canvas.pack()

#PanedWindows

p = PanedWindow(fenetre, orient=HORIZONTAL)
p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
p.add(Label(p, text='Volet 1', background='blue', anchor=CENTER))
p.add(Label(p, text='Volet 2', background='white', anchor=CENTER) )
p.add(Label(p, text='Volet 3', background='red', anchor=CENTER) )
p.pack()

fenetre.mainloop()