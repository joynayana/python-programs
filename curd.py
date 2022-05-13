import pymysql
x=pymysql.connect(host="localhost",user="root",password="nayanajoy01",db="avodha")
cr=x.cursor()
print('table content')

cr.execute('select * from example')
out1=cr.fetchall()
for i in out1:
    print(i)
    
nm=input('enter a name you wanted to search:')
cr.execute('select * from example where name=%s',nm)
out2=cr.fetchone()
print(out2)

pl=input('enter place you wanted to change:')
cr.execute('update example set place=%s where name=%s',(pl,nm))
cr.execute('select * from example')
out3=cr.fetchall()
for i in out3:
    print(i)

nm2=input('enter name you wanted to delete:')
cr.execute('delete from example where name=%s',nm2)
x.commit()
cr.execute('select * from example')
out4=cr.fetchall()
for i in out4:
    print(i)

x.commit()
x.close()
