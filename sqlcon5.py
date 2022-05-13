import pymysql
print('--view database--')
x=pymysql.connect(host='localhost',user='root',password='nayanajoy01',database='avodha')
cr=x.cursor()
a='select * from teachers'
cr.execute(a)
output=cr.fetchall()
print('HERE IS THE DETAILS')
for i in output:
    print(i)
x.commit()
x.close()
