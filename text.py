from tkinter import *
t=Tk()
t.geometry('500x500')
sc=Scrollbar()
sc.pack( side = RIGHT, fill = Y )
tx1=Text(height=10,width=30,yscrollcommand=sc.set)
tx1.place(x=12,y=23)
a='hai welcome nayana you can do ithai welcome nayana you can do ithai welcome nayana you can do ithai welcome nayana you can do ithai welcome nayana you can do ithai welcomenayana you can do ithai welcome nayana you can do ithai welcome nayana you can do ithai welcome nayana yohai welcome nayana you can do itvvvvvvvvvvvvu can do ithai welcome nayana you can do it'


def abcd():
    sc.config(command=tx1.yview)
    tx1.delete('1.0',END)
    tx1.insert(INSERT,a)
def clr():
    tx1.delete('1.0',END)
    
Button(text='view',command=abcd).place(x=50,y=200)

Button(text='clear',command=clr).place(x=120,y=200)
t.mainloop()
