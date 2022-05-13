from tkinter import *
import pymysql
x=pymysql.connect(host='localhost',user='root',password='nayanajoy01',db='avodha')
cur=x.cursor()
t=Tk()
#first label and textbox
Label(text="NAME:").place(x=15,y=34)
e1=Entry()
e1.place(x=60,y=34)
#second label and text box
Label(text="AGE:").place(x=15,y=80)
e2=Entry()
e2.place(x=58,y=80)
def store():
    text1=e1.get()
    text2=e2.get()
    cur.execute('insert into sample values(%s,%s)',(text1,text2))
    x.commit()
    x.close()
    t.destroy()
Button(text="SUBMITT",command=store).place(x=80,y=140)


t.mainloop()
