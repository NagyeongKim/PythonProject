import cx_Oracle
from matplotlib.pyplot import connect


#연결
conn = cx_Oracle.connect('scott','tiger','192.168.1.10:1521/XE')

cursor = conn.cursor()

cursor.execute("select * from emp") # 세미콜론 안적음


job = input("직업을 입력하세요 : ")

for item in cursor:
    if item[2] == job:
        print(item[1],item[2])

# for item in cursor:
#     print(item[1],item[5])


conn.close()



