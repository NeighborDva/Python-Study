#반복문
# for i in range(10): # range(1,10)-> 시작점 설정, 1~9출력됨
#     print(i)


# result = 0
# for a in range(1,101):#1~100
#     result = result + a
#     print(f"{a}.sum = {result}")

# print(result)


# result = 0
# for a in range(1,101):#1~100
#     result = result + a
#     print(f'{a} : sum = {result}')
#     if result > 100:
#         #print(f'{a} : sum = {result}')
#         break

# print(result)



# index = 0
# s = "BlockDMask"
# for a in s:
#     print(a,end=' ')
#     if a == 'k':
#         break #k를 찾았으니 for문에서 나와랏!

#     index = index + 1

# print(index)



# student = [180, 170, 164, 199,182,172,177]
# for a in student:
#     if a > 170: #조건을 반대로 하고 출력하는걸로 하면 결과값 같게 나옴
#         continue #키가 170보다 크면 continue

#     print(a)

# I = ['Alice','Bob','Charlie']

# for name in I:
#     if name == 'Bob':
#         print("Break!")
#         break
#     print(name)
# else: #break로 종료되면 else문 실행 x
#     print("!! Finish")

# sr = ['father', 'mother', 'brother']
# cnt = 0
# for s in sr:
#     print(s)
#     for c in s:
#         print(c,end=" ")
#         if c == 'r':
#             print(" ")
#             cnt += 1

# print(cnt)


# a = []

# for i in range(10):
#     a.append(i)

# print(a)

# a = []

# for i in range(3):
#     line = []
#     for j in range(2):
#         #line.append(j+1)
#         line.append(j+i)
#     a.append(line)

# print(a)

# for i in range(10,0,-3):
#     print(i)

I = ['Alice','Bob','Charlie']

for name in I:
    print(name)

for i, name in enumerate(I,42): #,42이런식으로 시작번호 지정가능
    print(i, name)