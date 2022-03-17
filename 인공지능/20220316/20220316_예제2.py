#기초연산자
#리스트-배열->변수 즉 안에 있는 값이 변경될 수 있음 , 튜플-배열이지만 상수라서 변경불가
#전체선택후 control+k -> control +c 전체 주석, control + u 전체 주석 해제

from __future__ import print_function
from math import remainder


print(4/3)
print(1/2)
print(4/2)
print(int(4/2)) #계산결과 정수형으로 나옴
print(7//3) #나머지 버리고 몫만
print(7%3) #나머지만, 주로 홀 짝 구분시에 많이 사용
print(2**10) #파이썬에서 제공하는 기본 제곱 연산자

print(' ')

#대입연산자1
a=1024
print(a)

a+=1024
print(a)

a-=1024
print(a)

a*=4
print(a)

a/=2
print(a)

a//=2
print(a)

a%=1022
print(a)

a**=10
print(a)

print(' ')

#divmod - 몫과 나머지를 한번에 얻을 수 있는 함수
quotient, remainder = divmod(5,2)
print(quotient,remainder)

print(' ')

#산술연산자
a= 11 + 2
b= 12 - 2
c= 13 * 2
d= 14 / 2
e= 15 ** 2
f= 16 // 2
g= 17 % 3
#전치, 후치 연산자는 사용불가하니 유의하자!
print(a,b,c,d,e,f,g)

#대입연산자2
i=3
i+=3 #대입연산은 print에서 바로 출력 불가하니 유의
print(i)

i-=3
print(i)

i*=2 #** 하면 9
print(i)

i /=2 #나누기 연산자는 기본적으로 실수형이 나온다. 그래서 int(i)를 한번 더 해주어야 정수형 확인이 가능
print(i)

i //= 2 #%하면 1.0 나옴 but 정수형으로 초기화 한상태로 % 수행하면 1나옴
print(i)

i=3
i %=2
print(i)

#관계 및 논리 연산자
a = 10
b = 3
print("10 == 3 =>",a==b)
print("10 != 3 =>",a!=b)
print("10 > 3 =>",a>b)
print("10 >= 3 =>",a>=b)
print("10 < 3 =>",a<b)
print("10 <= 3 =>",a<=b)
print()

#비트 연산자
a =13
print(bin(a)) #2진수
print(hex(a)) #16진수

print(0b1101) #이진수 입력시 10진수로 출력됨
print(int('1101',2)) #이진수를 10진수로 변환해주는 함수 int('2진수 문자열', 2)
print(" ")
#비트 논리 연산자
# AND
print(bin(0b1101 & 0b1001))
print(13 & 9)

# OR
print(bin(0b1101 | 0b1001))
print(13 | 9)

# XOR
print(bin(0b1101 ^ 0b1001))
print(13 ^ 9)

# AND
print(bin(~0b1101))
print(~13)

