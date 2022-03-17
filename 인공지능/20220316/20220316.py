#Python print함수 사용법 예제-201732049 제현승

print("Hello") 
print('hello', 'everyone')
print('hello'+'everyone') #붙여서 출력

print('Hello',end='') #end 이용시 자동으로 적용되던 줄바꿈 되신 end에 입력된 걸로 `바뀜`
print('test')

a = 123
b = 'hello'
print(a,b)
print(a,456,b,'world')

print('Hello Python!')
print("Nice to meet you.")
print('Hello "Python"')
print("Hello 'Python'")
print('Hello', 'Python!')
print('Hello'+ 'Python!')

print("화면에 직접 출력")
print('ab\'c')
print("ab'c")
print("doesn't")
print('does')
print('doesn\'t')
print("'string'")
print("\"string\"")
print('"string"')

s1='화면에 직접 출력'
s2='ab\'c'
s3='does'

print(s1)
print(s2)
print(s3)
print(s1[0]) #첫글자
print(s2[1]) #두 번째 글자
print(s3[1:3]) #2(1)~3(2)째 글자
print(s3[-1]) #마지막 글자
print(s3[-2]) #뒤에서 두 번째

a=2
b=3.14
c=a+b

print(a)
print(b)
print(c)

print(round(c,2)) #소숫점 두번째 자리까지만 표시, 반올림 조건이면 반올림된 결과 출력(3.1456에 3번째 짜리까지 출력하게 하면 3.146출력)
print("%.2f" %(c))#소숫점 두번째 자리까지만 표시,반올림 조건이면 반올림된 결과 출력(3.1456에 3번째 짜리까지 출력하게 하면 3.146출력)
print(a+b)
print(a,b,a+b,c)
d = 1e2
e=1e-2
print(d)
print(e) 

#숫자 문자 구분 못함
item1 = '사과'
price1 = 1000
item2 = '바나나'
price2 = 500
str1 = '{0}는 {1}원입니다.'
print(item1, price1)
print(item2, price2)

print(str1.format(item1,price1))
print(str1.format(item2,price2))
