import pymysql
x=pymysql.connect(host="localhost",user='root',password='nayanajoy01',db='avodha')
cur=x.cursor()
a=input("enter library name:")
b=input("enter place:")
c=int(input("enter entry fees:"))
cur.execute('insert  into library values(%s,%s,%s)',(a,b,c))
x.commit()
x.close()

