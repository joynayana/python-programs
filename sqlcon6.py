import pymysql
print('customised input')
x=pymysql.connect(host='localhost',user='root',password='nayanajoy01',database='avodha')
cr=x.cursor()
y=int(input('enter your age limit:'))
a='select * from customer where age<=%s'
cr.execute(a,y)
output=cr.fetchall()
for i in output:
    print(i)
x.commit()
x.close()
