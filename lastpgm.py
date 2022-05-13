from tkinter import *
t=Tk()
t.geometry('800x500')
#label and entry for name
Label(text="NAME:").place(x=10,y=10)
nm=Entry()
nm.place(x=55,y=12)

#label and entry for age
Label(text="age:").place(x=10,y=35)
ag=Entry()
ag.place(x=55,y=37)

#insert value to the table sample
def abcd():
    import pymysql
    x=pymysql.connect(host='localhost',user='root',password='nayanajoy01',db='avodha')
    cur=x.cursor()
    n=nm.get()
    a=ag.get()
    cur.execute('insert into sample values(%s,%s)',(n,a))
    x.commit()
    x.close()
Button(text='Submit', command=abcd).place(x=40,y=65)

#label and entry for update age corresponding name
Label(text="Update", fg='red',bg='black',font=('times new roman',24,'bold')).place(x=10,y=100)
Label(text="enter name to update:",fg='white',bg='black').place(x=5,y=155)
nu=Entry()
nu.place(x=150,y=157)
Label(text="enter new age:",fg='white',bg='black').place(x=5,y=200)
au=Entry()
au.place(x=150,y=202)

#function for updating value
def upd():
    import pymysql
    x=pymysql.connect(host='localhost',user='root',password='nayanajoy01',db='avodha')
    cur=x.cursor()
    nn=nu.get()
    na=au.get()
    cur.execute('update sample set age=%s where name= %s',(na,nn))
    x.commit()
    x.close()
Button(text='apply',command=upd).place(x=200,y=280)
#selecting value from sample and displaying it in to text with scrollbar
sc=Scrollbar()
sc.pack(side=RIGHT,fill=Y)
tx1=Text(height=20,width=40,yscrollcommand=sc.set)
tx1.place(x=350,y=23)
tx1.insert(INSERT,('click view to details'))                   
def data():
    sc.config(command=tx1.yview)
    import pymysql
    x=pymysql.connect(host='localhost',user='root',password='nayanajoy01',db='avodha')
    cur=x.cursor()
    cur.execute('select * from sample')
    n=cur.fetchall()
    vn=[','.join(map(str,xd))for xd in n]
    tx1.delete('1.0',END)
    tx1.insert(INSERT,('DATA SET \n---------\n'))   
    for i in vn:
        tx1.insert(INSERT,('%s\n\n'%i))
    x.close()
            
Button(text='view data',command=data).place(x=500,y=400)
#for clearing data
def clr():
    tx1.delete('1.0',END)
    
Button(text='clear',command=clr).place(x=590,y=400)
t.mainloop()
