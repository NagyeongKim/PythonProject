
import re
import fuction_fruit as ff
fruitlist=[{'name': '사과', 'price': 3000, 'cnt': 5},
          {'name': '포도', 'price': 4000, 'cnt': 20},
          {'name': '수박', 'price': 10000, 'cnt': 5} ]

SUM=0
while True:
    choice=input('''
        다음 중에서 하실 일을 골라주세요 :
        I - 입력
        S - 판매
        C - 재고리스트
        D - 삭제
        Q - 종료
        ''').upper()

    if choice=="I":  
        fruit = {'name': '', 'price': 0, 'cnt': 0} #체크
        while True:
            while True:
                fruit['name'] = input('과일 이름 >>> ')
                if fruit['name'].isalpha():
                    break
                else:
                    print('과일 이름을 정확하게 입력하세요.')
            check = 0
            for i in fruitlist:
                if i['name'] == fruit['name']:
                    check = 1
                    break
            if check == 0:
                break
            print('중복되는 과일 이름이 있습니다.')
        
        while True:
            fruitprice = input('가격 >>> ')
            if fruitprice.isnumeric():
                break
        fruit['price'] = int(fruitprice)

        while True:
            fruitcnt = input('수량 >>> ')
            if fruitcnt.isnumeric():
                break
        fruit['cnt'] = int(fruitcnt)
                    
        fruitlist.append(fruit)
        page = len(fruitlist)-1
        print(fruitlist)

    if choice=="S": 
        SUM= ff.fruit_s(fruitlist,SUM)


    elif choice == 'C':
        ff.fruit_c(fruitlist)

    elif choice == 'D':
        print(fruitlist)
        choice1 =input('삭제하려는 과일 이름을 입력하세요. >>> ')
        delok = 0
        for i in range(len(fruitlist)):
            if fruitlist[i]['name'] == choice1:
                print(f"{fruitlist[i]['name']}의 과일이 삭제되었습니다.")
                del fruitlist[i]
                delok = 1
                break
        if delok == 0:
            print('등록되지 않은 과일정보 입니다.')
        print(fruitlist)

    elif choice == "Q":
        print('프로그램을 종료합니다.')
        break