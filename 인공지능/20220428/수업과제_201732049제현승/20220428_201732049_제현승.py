import numpy as np

####집합_201732049 제현승
#### 중복된 원소 제거하기

a= [1,2,3]
b= [4,5,6]
c= [1,2,3,1,2]
d= [3,3,4,5,6,6,6,7,8,8,9]

print(a)
print(b)
print(d)

print()

###if not in 으로 중복된 원소 있는지 체크

new_c=[]
for i in c:
    if i not in new_c:
        new_c.append(i)

print(new_c)

new_d=[]
for i in d:
    if i not in new_d:
        new_d.append(i)

print(new_d)


#합집합 구현
#1.겹치는 원소가 없을 경우
a= [1,2,3]
b= [4,5,6]
c= a+b
print(c)

#2.겹치는 원소가 있을 경우
e = [1,2,3]
f=[2,3,4,5,6]
k=[]
for i in e:
    if i not in f:
        k.append(i)
print(k)
k= k+f
print(k)

#교집합 구하기
a= [1,2,3]
b= [2,3,4,5,6]
c=[]
for i in a:
    if i in b:
        c.append(i)
print(c)

#차집합 구현-겹치는 경우 합집합 구하는 과정의 for문과 동일
#c=a-b ->이렇게 하면 TypeError: unsupported operand type(s) for -: 'list' and 'list'에러 발생
a= [1,2,3]
b=[2,3,4,5,6]
c=[]
for i in a:
    if i not in b:
        c.append(i)
print(c)

#차집합-remove 사용
a= [1,2,3]
b=[2,3,4,5,6]
c=a+[] #a를 복사
for i in b:
    if i in a:
        c.remove(i);
print(c)

##여집합 구하기 
u = [1,2,3,4,5]
a=  [1,2,3]

a_com =[]
for i in u:
    if i not in a:
        a_com.append(i)
print(a_com)

##remove 사용
u = [1,2,3,4,5]
a=  [1,2,3]
rest = u + []
for i in u:
    if i in a:
        rest.remove(i)
print(rest)

##소수 알아보기 ※소수: 자기 자신과 1로 밖에 안나누어 지는 숫자, 1은 제외

a =17
a_prime = True
for i in range(2,a):
    if a % i == 0:
        a_prime = False
if a_prime == True:
    print("%d는 소수이다." %a)
else:
    print("%d는 소수가 아니다." %a)

#약수 찾기
a= 24
b= range(1,a)
factors =[]
for i in b :
    if a % i ==0:
        factors.append(i)
factors.append(a)
print(factors)

#최대 공약수 찾기
#1. 각 수의 약수를 모두 구한다.
#2. 겹쳐지는 수를 구하여 오름차순으로 정렬한다.
#3. 마지막 숫자가 최대 공약수이다.

#1
a= 24
aa= range(1,a)
a_factors =[]
for i in aa :
    if a % i ==0:
        a_factors.append(i)
a_factors.append(a)
print(a_factors)

b= 36
bb= range(1,b)
b_factors =[]
for i in bb :
    if b % i ==0:
        b_factors.append(i)
b_factors.append(b)
print(b_factors)

#2
common= []
for i in a_factors:
    if i in b_factors:
        common.append(i)
#3
common.sort()
print(common[-1]) #[-1]은 리스트의 마지막 원소를 가르킴

#최소 공배수 찾기, ※최소 공배수: 두 수의 곱을 최대 공약수로 나눈 수
#1. 두 수의 곱을 구한다.
#2. 두 수의 최대공약수를 구한다.
#3. 두 수의 곱을 최대공약수로 나눈다.

a= 24
b= 36
#1
M= a*b
#2, 최대공약수는 위의 프로그램에서 구함
GCD = common[-1] 
LCM = M/GCD
print('%d 와 %d 의 최소 공배수는 %d이다. ' %(a,b,LCM))
