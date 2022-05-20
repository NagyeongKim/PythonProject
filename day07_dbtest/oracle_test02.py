import cx_Oracle
from matplotlib.pyplot import connect


#연결
conn = cx_Oracle.connect('scott','tiger','192.168.1.10:1521/XE')

cursor = conn.cursor()

name = input("사원의 이름을 입력하세요: ")


sql= 'select * from emp where ename like :name'


#cursor.execute("select * from emp where ename '%'") # 세미콜론 안적음

cursor.execute(sql,name=name)

for item in cursor:
        print(item[1],item[5])

# for item in cursor:
#     print(item[1],item[5])


conn.close()


# 1. EMP 테이블에 job을 입력받아 해당 job인 사원을 출력하세요

# 2. 사원의 이름의 일부를 입력받아서 검색해서 출력



