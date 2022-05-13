import pymysql
print('inserting data')
x=pymysql.connect(host='localhost',user='root',password='nayanajoy01',database='avodha')
cur=x.cursor()
a='insert into student values("arathy",28)'
cur.execute(a)
x.commit()
x.close()
