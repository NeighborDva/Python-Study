# #입력문
# str = input("How old are you: ")
# print(str+" years old")
# print(str,"years old",sep=' ')

#정수 입력
# x = int(input('number: '))
# print(x)

#실수 입력

# x = float(input('number: '))
# print(x)

# #입력받은 문자 숫자로 변경 eval
# year = input("This year: ")
# year = eval(year) #정수, 실수 가능(원하는 수로 입력하면 됨)
# year = year + 1
# print("Next year:",year)
# #year = eval(input("This year: ")) 도가능



i=0
result = 0
while i<5:
    print(f"{i+1}번째",end=" ")
    a=input("성적 입력 : ")
    result += int(a)
    i += 1

print(f'평균 : {result / 5}')