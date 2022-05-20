import re 


def fruit_s(fruitlist,SUM):

        while True:
            print("----------판매항목--------------")
            print(fruitlist)
            choice1 = input('어떤 항목을 판매할까요? >>>')
            choice2=  int(input('몇 개를 판매할까요? >>>'))
            
            while choice2 > 0: 
                for i in fruitlist:
                    if i['name'] == choice1:
                        if choice2 >=0 and choice2 <= i['cnt']:
                            print('good')
                        
                        else:
                            print('판매할 수 있는 최대 수량은',i['cnt'],'입니다')
                            print('다시 입력해주세요 ')
                            choice2=  int(input('몇 개를 판매할까요? >>>'))

                break
                        
               

            for i in range(len(fruitlist)):
                if fruitlist[i]['name'] == choice1:
                    print(fruitlist[i]['name'], " 항목을 판매합니다. >>>")
                    fruitlist[i]['cnt'] -= choice2
                    SUM += fruitlist[i]['price'] * choice2
                    print("총 판매금액 : ", SUM)

  
                print("추가적으로 판매하실 항목이 있으십니까? >>>")
                sale_ans= input("Y/N : ").upper()
                if sale_ans == 'Y':
                    choice1 = input('어떤 항목을 판매할까요? >>>')
                    choice2=  int(input('몇 개를 판매할까요? >>>'))
                    for i in range(len(fruitlist)):
                        if fruitlist[i]['name'] == choice1:
                            print(fruitlist[i]['name'], " 항목을 판매합니다.")
                            fruitlist[i]['cnt'] -=choice2
                            SUM += fruitlist[i]['price'] *choice2
                            print("총 판매금액 : ", SUM)

                else :
                    print("총 판매금액 : ", SUM)
                    break
            break
        
        return SUM


def fruit_c(fruitlist):
        print("재고 리스트 출력합니다.")
        print("-------------------------")
        for i in range(len(fruitlist)):
            print('name: ', fruitlist[i].get('name'),' cnt: ', fruitlist[i].get('cnt'), ' price:', fruitlist[i].get('price'))

        print("-------------------------")    

