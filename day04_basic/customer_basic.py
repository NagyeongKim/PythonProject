# 콘솔형 고객 정보 관리 시스템 구축

# 1. 기능
# 고객 정보 입력(I) , 현재/이전/다음 고객 정보 조회 (C/P/N), 고객 정보 수정(U) , 고객 정보 삭제(D) , 고객 정보 종료



'''
괄호 안 영문자를 입력하면 각 기능이 구현학 ㅔ만든다. 

종료 Q를 입력하기 전까지 기능 선택 메시지가 계속 뜨도록 만든다.

각 기능은 함수로 관리한다.

입력된 각 정보는 인덱스 값에 따라 페이지를 가진다.

-> 첫 정보 입력시 인덱스는 0이므로, 입력전 기본 page 값은 -1로 설정한다.

'''

# 2. 입력(I)
# dictionary로 각 키의 값을 받고 빈 리스트에 채워나간다. 
# 성별(gender) : M,m,F,f 로만 입력 가능
# -> 소문자로 입력하는 경우 대문자로 자동 변환
# -> gender 값이 M , m , F, f 로만 입력 가능 
# 이메일(email) : 입력값 내에 '@'가 반드시 있어야 함
# -> 정규표현식 사용
# -> re를 import 하여 이메일 입력값 내 '@' 존재 여부 파악
# -> 없는 경우 '@'를 포함하라는 문구와 함께 재입력 하도록 함
# -> 중복된 이메일 입력 방지
# 출생년도(birthyear) : 4자리로 입력해야 
# -> len 값으로 입력 값의 길이를 구함
# -> 4자리가 아닐 경우 재입력 하도록 함
# 출생년도까지 입력이 완료되었을 경우 
# -> 키 값 입력이 완료된 customer 딕셔너리를 custlist 리스트에 추가(append) 한다.
# -> 고객 정보가 새로 입력 되었으므로 page 값에 1를 더한다. 

# 3.조회(C,P,N)
# - 인덱스는 0부터 시작하나 페이지는 통상 1부터 시작하므로 페이지 출력
# - 이전 페이지 조회(p)의 경우, 첫번째 페이지인 상태에서 



import re
custlist= []

custlist = [{'name' : '홍길동', 'gender':'M', 'email':'hong123@gmail.com','birthyear':'12345'}]

page = 2

while True:
    choice = input("다음 중 하실 일을 골라주세요").upper()

    if choice == 'I':
        customer = {'name': '', 'gender':'' , 'email':'', 'birthyear':''}
        customer['name']=input('이름>>>')
        while True:
            customer['gender'] = input('성별(M,F) >>> ').upper()
            if customer['gender'] in ('M,F'):
                break
        while True:
            while True:
                customer['email'] = input('email >>> ')
                if customer['email'].find('@') != -1:
                    break
                else:
                    print('이메일을 정확하게 읿력하세요')
            check = 0
            for i in custlist:
                if i['email'] == customer['email']:
                    check = 1
                    break
            if check == 0:
                break
            print("중복되는 이메일이 있습니다.")
            while True:
                customer['birthyear']= input('생년월일(4자리)')
                if len(customer['birthyear']) == 4 and customer['birthyear'].isdecimal()
                    break

            custlist.append(customer)
            page = len(custlist) - 1 
            print(custlist)
    elif choice == 'C':
        if page < 0:
            print("입력된 정보 x")
        else : 
            print(f"현재 페이지는 {page+1}페이지 입니다.")
            print(culstlist({page}))
    elif choice == 'P':
        if page <= 0:
            print("마지막 페이지")
        else:
            page += 1
            print(custlist[page])
    elif choice == 'N':

    elif choice == 'D':

    elif choice == 'U':
        
    elif choice == 'Q':
        print("프로그램 종료")
        break
        
                    
