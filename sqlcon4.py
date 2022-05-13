import pymysql
x=pymysql.connect(host="localhost",user="root",password="nayanajoy01",database="avodha")
cur=x.cursor()
print('CUSTOMER DATAILS COLLECTION CENTER')
a=input('Enter customer name:')
b=input('Enter cutomer age:')
c=input('Enter customer place:')
cur.execute('insert into customer values(%s,%s,%s)',(a,b,c))
x.commit()
data='select * from customer where name=%s'
cur.execute(data,a)
output=cur.fetchall()
for i in output:
    print(i)
x.close()
