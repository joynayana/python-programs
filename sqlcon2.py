import pymysql
print('inserting data')
x=pymysql.connect(host='localhost',user='root',password='nayanajoy01',database='avodha')
cur=x.cursor()
cur.execute('insert into student values("arun jose",30)')
x.commit()
x.close()
