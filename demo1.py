from tkinter import *
import tkinter.messagebox
import pymysql
root=Tk()
root.title("customer Data")
root.geometry('500x500')


def load():
    text1=e1.get()
    x=pymysql.connect(host="localhost",user="root",password="nayanajoy01",db="nayana")
    cur=x.cursor()
    cur.execute('select place,address from data where name=%s',text1)
    if cur.rowcount==0:
        e2.delete(0, END)
        e3.delete(0, END)
        tkinter.messagebox.showinfo('info','sorry! this name is not present in the table')
    else:
        out=cur.fetchone()
        print(type(out))
        e2.insert(END,out[0])
        e3.insert(END,out[1])
        x.commit()
        x.close()
        

l1=Label(text="Name:")
l1.place(x=0,y=40)
e1=Entry()
e1.place(x=60,y=40)
b1=Button(text="click here to load below details",bg="brown",fg="white",command=load)
b1.place(x=200,y=40)

l2=Label(text="Address:")
l2.place(x=0,y=120)
e2=Entry()
e2.place(x=60,y=120)

l3=Label(text="place:")
l3.place(x=0,y=160)
e3=Entry()
e3.place(x=60,y=160)
root.mainloop()
