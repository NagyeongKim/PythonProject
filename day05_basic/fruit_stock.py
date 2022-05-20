import re


# 과일가게 재고 프로그램
# - 재고 입력
# - 판매 
# - 재고 상황 리스트 출력
# - 삭제 처리


# 콘솔형 고객 정보 관리 시스템 구축

# 1. 기능  
# 고객 정보 입력(I), 현재/이전/다음 고객 정보 조회(C/P/N), 고객 정보 수정(U), 고객 정보 삭제(D), 고객 정보 종료(Q)

# - 괄호 안 영문자를 입력하면 각 기능이 구현되게 만든다
# - 종료(Q)를 입력하기 전까지 기능 선택 메시지가 계속 뜨도록 만든다
# - 각 기능은 함수로 관리한다
# - 입력된 각 정보는 인덱스 값에 따라 페이지를 가진다
#   -> 첫 정보 입력 시 인덱스는 0이므로, 입력 전 기본 page 값은 -1로 설정한다

# 2. 입력(I)
# - dictionary로 각 키의 값을 받고 빈 리스트에 채워나간다
# - 성별(gender) : M, m, F, f로만 입력 가능
#   -> 소문자로 입력하는 경우 대문자로 자동 변환
#   -> gender 값이 M 또는 F가 아닐 경우 다시 입력
# - 이메일(email) : 입력값 내 '@'가 반드시 있어야 함
#   -> 정규표현식 사용
#   -> re를 import 하여 이메일 입력값 내 '@' 존재 여부 파악
#   -> 없는 경우 '@'를 포함하라는 문구와 함께 재입력 하도록 함
#   -> 중복된 이메일 입력 방지
# - 출생년도(birthyear) : 4자리로 입력 해야
#   -> len 값으로 입력 값의 길이를 구함
#   -> 4자리가 아닐 경우 재입력 하도록 함
# - 출생년도까지 입력이 완료되었을 경우
#   -> 키 값 입력이 완료된 customer 딕셔너리를 custlist 리스트에 추가(append)한다
#   -> 고객 정보가 새로 입력 되었으므로 page 값에 1을 더한다

# 3. 조회(C, P, N)
# - 인덱스는 0부터 시작하나 페이지는 통상 1부터 시작하므로 페이지 출력시 page+1 값을 반환한다
# - 이전 페이지 조회(P)의 경우, 첫 번 째 페이지인 상태에서 이전 페이지로 이동이 불가하므로 현재 페이지인 첫 번 째 페이지를 반환
# - 다음 페이지 조회(N)의 경우, 마지막 페이지인 상태에서 다음 페이지로 이동이 불가하므로 현재 페이지인 마지막 페이지를 반환

# 4. 삭제(D)
# - unique한 키를 기준으로 삭제정보를 선택한다 -> 여기서는 이메일로 가정
# - 삭제 성공 여부 변수(delok)
#   -> 입력한 이메일이 등록된 정보 내에 있을 경우 삭제
#   -> 삭제가 성공하면 delok=1 (default 값 0)
#   -> 등록된 정보 내에 없는 이메일일 경우(delok=0) 등록되지 않았다고 출력

# 5. 수정(U)
# - unique한 키를 기준으로 수정 정보를 선택한다 -> 여기서는 이메일로 가정
# - 입력한 이메일과 일치하는 고객 정보의 인덱스를 idx에 입력
#   -> idx의 default 값은 -1
#   -> 일치 여부 확인 후에도 idx가 -1일 경우 등록되지 않았다고 출력
# - 이메일 외에 이름, 성별, 출생년도 중 수정할 정보 선택
# - 수정할 정보 선택 후 수정할 내용 입력
# - 수정하고 픈 변수가 없는 경우 exit 입력 시 수정 창 종료

# 6. 종료(Q)
# - 맨 처음 while 반복문을 나간다 -> break


import re
fruitlist=[]

fruitlist=[{'name': '사과', 'price': 3000, 'cnt': 5},
          {'name': '포도', 'price': 4000, 'cnt': 20},
          {'name': '수박', 'price': 10000, 'cnt': 5} ]

while True:
    choice=input('''
        다음 중에서 하실 일을 골라주세요 :
        I - 입력
        S - 판매
        C - 재고리스트
        D - 고객 정보 삭제
        ''').upper()  

    #입력    
    if choice=="I":  
        customer={'name': '', 'price': '', 'cnt': ''}
        customer['name']=input('이름 >>> ')
        while True:
            customer['gender']=input('성별(M,F) >>> ').upper()
            if customer['gender'] in ('M','F'):
                break
        while True:
            while True:
                customer['email']=input('email >>> ')
                if customer['email'].find('@') != -1:
                    break
                else:
                    print('이메일을 정확하게 입력하세요')
            check = 0
            for i in custlist:
                if i['email'] == customer['email']:
                    check = 1
                    break
            if check == 0:
                break
            print('중복되는 이메일이 있습니다.')
        while True:
            customer['birthyear'] = input('생년월일(4자리) >>> ')
            if len(customer['birthyear']) == 4 and customer['birthyear'].isdecimal():
                break

        custlist.append(customer)

        print(custlist)
            
    #판매
    elif choice=="S": 
            while True:
                choice1 = input('어떤 항목을 판매할까요?')
            
                print(fruitlist)



    elif choice=='D':
        print(custlist)
        choice1 = input('삭제하려는 이메일 주소를 입력하세요 >>> ')
        delok = 0
        for i in range(len(custlist)):
            if custlist[i]['email'] == choice1:
                print(f'{custlist[i]["name"] }님의 정보가 삭제되었습니다.')
                del custlist[i]
                delok = 1
                break
        if delok == 0:
            print('등록되지 않은 고객 정보입니다.')
        print(custlist)

  

    elif choice=="Q":
        print('프로그램을 종료합니다.')
        break