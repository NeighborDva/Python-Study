# #조건문
# #파이썬에서 조건문은 들여쓰기가 중요

# name = "Je"
# if name == "Je":
#     print("이름이 맞습니다.")
# else:
#     print("이름이 틀립니다.")

# pocket = 100
# if pocket == 500:
#     print("복권구매")
# elif pocket == 100:
#     print("껌 구매")
# else:
#     print("집")

# a= "사과"
# b= "바나나"
# c="치즈"

# if a == "사과" or b== "오바나나":
#     print("사과이거나 바나나입니다.")

# if a == "사과" or b== '바나나': #파이썬은 ' " 구분하지 않음
#     print("사과이거나 바나나입니다.")

# if not c == "사과": #사과인 a로 하면 논리연산 결과가 false이기 때문에 실행되지 않음
#     print("사과가 아니어야 합니다.")

# a = [1,2,3,4,5,6,7,8,9,10] #상수가 들어 있는 튜플
# if 1 in a:
#     print("a 리스트에 1이 포함되어 있습니다.")
# if 10 in a:
#     print("a 리스트에 10이 포함 되어있습니다.")

# p_class = "Z"
# sel_amount = 79900

# if p_class == "A":
#     sel_amount *= 0.7 #55930.0
#     print(sel_amount)
# elif p_class == "B": #67915.0
#     sel_amount *= 0.85
#     print(sel_amount)
# elif p_class == "C": #73508.0
#     sel_amount *= 0.92
#     print(sel_amount)
# elif p_class == "Z": #84900
#     sel_amount += 5000
#     print(sel_amount)

# p_class = "Z"
# sel_amount = 79900

# if p_class == "A":
#     sel_amount *= 0.7 #55930.0
#     print(f'판매가는 {sel_amount}원 입니다.')
# elif p_class == "B": #67915.0
#     sel_amount *= 0.85
#     print(f'판매가는 {sel_amount}원 입니다.')
# elif p_class == "C": #73508.0
#     sel_amount *= 0.92
#     print(f'판매가는 {sel_amount}원 입니다.')
# elif p_class == "Z": #84900
#     sel_amount += 5000
#     print(f'판매가는 {sel_amount}원 입니다.')
#     print('판매가는 %f원 입니다.' %sel_amount)     

# x = 11
# if x < 10:
#     print('x는 10보다 작아!')
# else:
#     print('x는 10보다 작지 않아!')

# x=2
# if x%2 == 0:
#     print('x는 짝수야!')#EvenNumber
# else:
#     print('x는 홀수야!') #Odd Number

# x = 3
# if x < 10:
#     print('x는 10보다 작아!')
#     if x%2 == 0:
#         print('x는 짝수야!')#EvenNumber
#     else:
#         print('x는 홀수야!') #Odd Number
# else:
#     print('x는 10보다 작지 않아!')
#     if x%2 == 0:
#         print('x는 짝수야!')#EvenNumber
#     else:
#         print('x는 홀수야!') #Odd Number

# x=12

# if x<10 and x%2 ==0:
#     print('x는 10보다 작으면서 짝수야!')
# if x<10 and not x%2 ==0:
#     print('x는 10보다 작으면서 홀수야!')
# if not x<10 and x%2 ==0:
#     print('x는 10보다 크면서 짝수야!')
# if not x<10 and not x%2 ==0:
#     print('x는 10보다 크면서 홀수야!')

##while문
# treehit = 0
# while treehit < 10:
#     treehit = treehit + 1
#     print("나무를 %d번 찍었습니다." %treehit)
#     if treehit == 10:
#         print("나무 넘어갑니다.")


##break문 추가
# coffee = 10
# money = 300
# while money:
#     print("돈을 받았으니 커피를 줍니다.")
#     coffee = coffee -1
#     #break #실행하자마자 바로  while문 종료
#     print("남은 커피의 양은 %d개입니다."%coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break

# while True:
#     print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.") #KeyBoard 인터럽트에 의해 빠져나옴

# i = 0
# result1 =0
# while i< 100:
#     i= i+1
#     if i%2 == 0:
#         print('1번 방법: {0} {1}'.format(i,result1))
#         result1 = result1 + i

# print('1번 방법: {0}'.format(result1))

# i = 0
# result2 =0
# while i< 100:
#     i= i+2 # 초깃 값이 뭐냐 에따라 더해질 i가 짝인지 홀인지 결정
#     print('2번 방법: {0} {1}'.format(i,result2))
#     result2 = result2 + i

# print('2번 방법: {0}'.format(result2))

j = 0
result3 =0
while True:
    if j>100:
        break
    j= j+1
    if j%2 == 0:
        print('3번 방법: {0} {1}'.format(j,result3))
        result3 = result3 + j

print('3번 방법: {0}'.format(result3))