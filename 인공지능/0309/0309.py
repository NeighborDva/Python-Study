watch = 100000
a = 'pig'
b = 'dad'

print(a)
print(b)
print(watch)
print(a+b)  #터미널이 아닌 파일이기 때문에 a+b만 쓰면 실행시 'pigdad' 출력안됨 그래서 꼭 명령을 써야함
print(a+' '+b)
'''
파이썬의 변수 선언법 a,b 이렇게 한문자로 선언하는 것보다 아래와 같은 방식으로 변수를 선언하는게 프로그램 이해에 도움이 될 수 있음
item_list - 스네이크 케이스, ItemList - 캐멀케이스 #첫문자가 대문자냐 소문자냐로 구분
'''

'''
변수 선언법
1. a=10
2.a,b=(10,20) 튜플을 이용하여 각각 값을 할당
3.[a,b] = [10,20] 리스트를 이용하여 각각 값을 할당, 단일 문자로 리스트 이용하면 배열 ex) a=[10,20] 그리고 일반변수 출력하듯이 출력하면 출력됨
4.a=b=10 a와 b에 똑같은 값을 할당하고 싶을때 사용
5.a=None : 비어있는 변수를 만들고 싶을 때 사용
'''

#변수교환예제 ㅍ 
aa = 1
bb = 100

aa,bb = bb, aa
print(aa)
print(bb)

'''
a,b = b,a 이런식으로 작성하면 교환 가능
'''

#배열예제
a1 = [10,20,30]
b1 = a1
a1[0] = 200
print(b1) #200 20 30 나옴 즉 b1에 a1을 대입이 먼저이지만 a1에 데이터 변화시 b1에도 적용

'''
print 숫자변수(a)와 문자열 변수 조합
1.print("a="+str(a)) str함수를 사용해 a를 문자열 변환
2.print("a=",a) 문자와 숫자 표시를 위해 ','콤마 사용
3.print("a={}".format(a)) format함수 사용 c를 format해서 괄호안에 나타냄
'''


#print 출력예제
print("Hello World")
print('Hello World')
print(1) #숫자
print("1") #문자 -but 콘솔에선 구분 불가

c=1
print("c="+str(c))
print("c=",c)
print("c={}".format(c)) 