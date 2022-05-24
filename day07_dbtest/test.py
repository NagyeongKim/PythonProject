import os 
import re
import cx_Oracle


# fruitlist=[{'name': '사과', 'price': 3000, 'cnt': 5},
#           {'name': '포도', 'price': 4000, 'cnt': 20},
#           {'name': '수박', 'price': 10000, 'cnt': 5} ]


#연결
conn = cx_Oracle.connect('scott','tiger','localhost/XE')



cursor = conn.cursor()
cursor.execute("drop table fruitlist")
#테이블만들기
cursor.execute("create table fruitlist(name varchar(20) not null, price number(10) not null, cnt number(10) not null)")


#데이터입력
cursor.execute("insert into fruitlist values('사과',3000,5)")


cursor.execute("insert into fruitlist values('포도',4000,20)")


cursor.execute("insert into fruitlist values('수박',10000,5)")



check_sql= "select * from fruitlist"
rs = cursor.execute(check_sql)
# name = input("어떤 항목을 판매할까요? >>>")
# cnt = int(input("몇 개를 판매할까요? >>>"))
# print(f"{name}을 {cnt}개 판매합니다.")
#한라인씩 읽음

col1 = []
col2 = []

for record in rs:
    col1.append(record[0])
    col2.append(record[1])
print("col1 : ", col1)
print("col2 : ", col2)


conn.commit()
conn.close()