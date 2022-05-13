import pymysql
print('--database pymysql connected to python---')
x=pymysql.connect(host='localhost',user='root',password='nayanajoy01',database='avodha')
cur=x.cursor()
cur.execute('create table student(name char(20),age int)')
x.close()
