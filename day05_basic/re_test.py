
# a = 'hello, world!'
# print(re.match('python',a))

# print(re.search('world',a))

# print(re.search('hello',a))


# '''
# 정규표현식에서 ^을 붙이면 문자열이 맨 앞에 오는지 판단하고,
# 문자열 뒤에 $를 붙이면 문자열이 맨 뒤에 오는지 판단한다. 

# 지정된 문자열이 하나라도 포함되는지 판단하기
# | 는 특정문자열에서 지정된 문자열이 하나라도 포함되는지 판단



# '''

#str1='asdfase25435AAVVGHR'

# '''
# [] 대괄호 안에 숫자 범위를 넣으며 * 또는 +를 붙인다. 
# *는 문자(숫자)가 0개 이상 있는지
# +는 1개 이상 있는지 판단

# '''

#print(re.match('[0-9]*', str1))

# '''
# 특정 문자 범위에 포함되지 않는지 판단하기 

# [^범위]*
# [^범위]+
# 가-힣|ㄱ-ㅎ|ㅏ-ㅣ
# '''

#같은 정규표현식 패턴을 자주 사용할 때
#매번 match나 search 함수에 정규표현식 패턴을 지정하는 방법은 비효율적입니다. 

import re
p = re.compile('^[a-z][a-z0-9_]{4,}@{3,}[.][a-z]{2,}$')
print(p.search('7up@mgmail.com'))

email = ''
while not p.search(email):
    email = input('email >>> ')
    
