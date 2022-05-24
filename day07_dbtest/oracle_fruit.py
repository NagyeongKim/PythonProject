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


while True:
        choice=input('''
        다음 중에서 하실 일을 골라주세요 :
        I - 입력
        S - 판매
        C - 재고리스트
        D - 삭제
        Q - 종료
        ''').upper()
        if choice == 'I':
            insert_sql = "insert into fruitlist values(:1,:2,:3)"
            name= input("과일 이름 >>> ")
            price= int(input("과일 가격 >>> "))
            cnt= int(input("과일 수량 >>> "))
            data = (name, price, cnt)
            cursor.execute(insert_sql, data)
            cursor.close()
            break

        if choice == 'S':
            check_sql= "select * from fruitlist"
            cursor.execute(check_sql)
            name = input("어떤 항목을 판매할까요? >>>")
            cnt = int(input("몇 개를 판매할까요? >>>"))
            print(f"{name}을 {cnt}개 판매합니다.")
            
            rows= cursor.fetchall()  # 이중리스트 형태로 담긴다.

            rows = [list(rows[x]) for x in range(len(rows))] #튜플 이중리스트로 바꾸기
            #print(rows)
            for i in range(len(rows)):
                for j in range(len(rows)):
                    if 
                    cnt = rows[i][j] -cnt
                    sales_sql= "update fruitlist set cnt = :1 where name = :2"
                    data = (cnt,name)
                    cursor.execute(sales_sql,data)
            break

conn.commit()
conn.close()
        






# SUM=0
# while True:
#     choice=input('''
#         다음 중에서 하실 일을 골라주세요 :
#         I - 입력
#         S - 판매
#         C - 재고리스트
#         D - 삭제
#         Q - 종료
#         ''').upper()

#     if choice=="I":  
#         fruit = {'name': '', 'price': 0, 'cnt': 0} #체크
#         while True:
#             while True:
#                 fruit['name'] = input('과일 이름 >>> ')
#                 if fruit['name'].isalpha():
#                     break
#                 else:
#                     print('과일 이름을 정확하게 입력하세요.')
#             check = 0
#             for i in fruitlist:
#                 if i['name'] == fruit['name']:
#                     check = 1
#                     break
#             if check == 0:
#                 break
#             print('중복되는 과일 이름이 있습니다.')
        
#         while True:
#             fruitprice = input('가격 >>> ')
#             if fruitprice.isnumeric():
#                 break
#         fruit['price'] = int(fruitprice)

#         while True:
#             fruitcnt = input('수량 >>> ')
#             if fruitcnt.isnumeric():
#                 break
#         fruit['cnt'] = int(fruitcnt)
                    
#         fruitlist.append(fruit)
#         page = len(fruitlist)-1
#         print(fruitlist)

#     if choice=="S": 
#         while True:
#             print("----------판매항목--------------")
#             print(fruitlist)
#             choice1 = input('어떤 항목을 판매할까요?')
#             choice2=  int(input('몇 개를 판매할까요?'))
            
#             while choice2 > 0: 
#                 for i in fruitlist:
#                     if i['name'] == choice1:
#                         if choice2 >=0 and choice2 <= i['cnt']:
#                             print('good')
                        
#                         else:
#                             print('판매할 수 있는 최대 수량은',i['cnt'],'입니다')
#                             print('다시 입력해주세요 ')
#                             choice2=  int(input('몇 개를 판매할까요?'))

#                 break
                        
                           
               

#             for i in range(len(fruitlist)):
#                 if fruitlist[i]['name'] == choice1:
#                     print(fruitlist[i]['name'], " 항목을 판매합니다.")
#                     fruitlist[i]['cnt'] -= choice2
#                     SUM += fruitlist[i]['price'] * choice2
#                     print("총 판매금액 : ", SUM)

  
#                 print("추가적으로 판매하실 항목이 있으십니까?")
#                 sale_ans= input("Y/N : ").upper()
#                 if sale_ans == 'Y':
#                     choice1 = input('어떤 항목을 판매할까요?')
#                     choice2=  int(input('몇 개를 판매할까요?'))
#                     for i in range(len(fruitlist)):
#                         if fruitlist[i]['name'] == choice1:
#                             print(fruitlist[i]['name'], " 항목을 판매합니다.")
#                             fruitlist[i]['cnt'] -=choice2
#                             SUM += fruitlist[i]['price'] *choice2
#                             print("총 판매금액 : ", SUM)

#                 else :
#                     print("총 판매금액 : ", SUM)
#                     break
#             break    



#     elif choice == 'C':
#         print("재고 리스트 출력합니다.")
#         print("-------------------------")
#         for i in range(len(fruitlist)):
#             print('name: ', fruitlist[i].get('name'),' cnt: ', fruitlist[i].get('cnt'), ' price:', fruitlist[i].get('price'))
            
#         print("-------------------------")         

#     elif choice == 'D':
#         print(fruitlist)
#         choice1 =input('삭제하려는 과일 이름을 입력하세요. >>> ')
#         delok = 0
#         for i in range(len(fruitlist)):
#             if fruitlist[i]['name'] == choice1:
#                 print(f"{fruitlist[i]['name']}의 과일이 삭제되었습니다.")
#                 del fruitlist[i]
#                 delok = 1
#                 break
#         if delok == 0:
#             print('등록되지 않은 과일정보 입니다.')
#         print(fruitlist)

#     elif choice == "Q":
#         print('프로그램을 종료합니다.')
#         break