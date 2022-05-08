# def func1():
#     print('BlockDMask')

# func1()
# func1()
# func1()

# def func2(a,b):
#     print(f'{a} 곱하기 {b} = {a*b}')

# func2(1,2)
# func2(2,3)
# func2(3,4)

# def func3():
#     return 'abcedfg'

# a= func3()
# print(a,"GG",sep=" ")

# def func4(a,b):
#     return a*b

# a = input()
# b= input()
# c= func4(int(a),int(b))
# print(c)

# for i in range(1,10):
#     print(f'2 * {i} = {2*i}')

# for i in range(1,10):
#     print(f'3 * {i} = {3*i}')

# print()
# print()
# print()

# def gugudan(num):
#     for i in range(1,10):
#         print(f'{num} * {i} = {num*i}')

# gugudan(2)
# gugudan(3)

# def func4(a,b=5,c=10):
#     return a+b+c

# print(func4(1,2,3))
# print(func4(1,2))
# print(func4(1))


# def func5(*args):
#     a=0
#     for i in args:
#         a= a+ i 
#     return a

# b = func5(1,5)
# print(b)
# c = func5(2,3,4,5)
# print(c)
# d = func5(1,2,3,4,5,4,3,2,1)
# print(d)

# e = func5()
# print(e)


# def test(*val):
#     for i in val:
#         print(i)

# test(1,'a','c',3)

# def sum_mul(choice, *val):
#     if choice == 'sum':
#         result = 0
#         for i in val:
#             result = result + i
#     elif choice == 'mul':
#          result = 1
#          for i in val:
#             result = result * i
#     return result

# print(sum_mul('sum',1,2,3,4,5))
# print(sum_mul('mul',1,2,3,4,5))

# def comp (score = 0):
#     if score ==0:
#         return 0
#     elif score > 50:
#         return 2
#     else:
#         return 1

# grade = comp(40)
# print("Grade is",grade," for ", 40)

# grade = comp(80)
# print("Grade is",grade," for ", 80)

# grade = comp()
# print("Grade is",grade," for no score")

# def report(name, age, score):
#     print(name,score)

# report(age=10,name="Kim",score=80)
# report("Kim",10,80)









