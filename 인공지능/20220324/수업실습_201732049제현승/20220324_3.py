#문자열 함수 Part1
# a = 'I Love Python'

#1.len

# print(len(a)) #공백도 문자열 취급

# b= 'abcd'
# print(len(b))

# c= 'a b c d'
# print(len(c))

# name = 'BlockDMask'
# phone = '010 xxxx xxxx'
# address = 'korea'

# print(len(name))
# print(len(phone))
# print(len(address))

#2.min

# a = [1, 2, 3]
# print(min(a))

# b = 'BlockDMask' #아스키 코드 값 으로비교
# print(min(b))

# c = 1 #값 1개 이면 에러, 리스트로 선언해야 min 사용가능
# #print(min(c))

# d =(6,5,4,2)
# print(min(d))

# e=[3,4,5,'a','b','c'] #데이터 타입 다르면 안됨
# #print(min(e)) 

#3.max

# a = [1, 2, 3]
# print(max(a))

# b = 'BlockDMask' #아스키 코드 값 으로비교
# print(max(b))

# c = 1 #값 1개 이면 에러, 리스트로 선언해야 max 사용가능
# #print(max(c))

# d =(6,5,4,2)
# print(max(d))

# e=[3,4,5,'a','b','c'] #데이터 타입 다르면 안됨
# #print(max(e)) 

#여러개의 문장간에도 해당 함수 사용가능-> 데이터 타입 동일해야함
# a=[1,2,3]
# b=[1,2,4]
# #b=[4,5,6]
# print(min(a,b))

# #'BBB' 랑 'BB'로 min 하면 BB 나옴 'BBB' 'BBa'면 BBB나옴
# c='BlockDMask'
# d='BAAAlockDMask'
# print(min(c,d))

# g = [2, 3, 4]
# h = [2,2,2,2,2]
# i = [9,8,7,6,5]
# j = [1]
# k = [0]
# print(min(g,h,i,j,k))

#4.count함수


# myString = "everdevel"
# print(myString.count('e'))#두글자도 가능

# a = 'BlockDMask'

# print('#1 a.count("k")')
# print(a.count('k'))
# print('#2 a.count("DM")')
# print(a.count('DM'))
# print("#3 a[2]+ '~'+a[4]")
# print(a[2] + '~' + a[4])
# print("#4 a.count('k',2,3)") #a.count('k',2,3) 검색범위 지정, 지정안하면 끝까지 모두 검색
# print(a.count('k',2,3))
# print("#5 a.count('k',2,4)")
# print(a.count('k',2,4))
# print("#6 a.count('k',2,5)")
# print(a.count('k',2,5))

#5.find, rfind

# str = "BlockDMascleark Blog."
# print(f"str: {str}\n")

# print("1.str.find('찾을 문자')")
# result1 = str.find('a')
# result1_2 = str.rfind('B') #오른쪽부터 탐색
# result1_3 = str.rfind('B',0,5) #count처럼 검색범위 지정
# print(result1)
# print(result1_2)

# #문자 없는 경우 테스트 -> -1 나옴
# result2 = str.find('z')

# print(f"str.find('a') : {result1}")
# print(f"str.find('z') : {result2}")

# #문자뿐만 아니라 단어도 가능

# result3 = str.find('ask')
# print(f"str.find('ask') : {result3}")

# print("2. str.find('찾을 문자', 시작index)") 
# result5 = str.find('o') 
# result6 = str.find('o', 5) 
# print(f"str.find('o') : {result5}") 
# print(f"str[5] : {str[5]}") 
# print(f"str.find('o', 5) : {result6}") 
# print()

#6.startswith ->검색 범위 지정가능

# str = "Hello world, Python!"
#print(len(str))
# if str.startswith('Hello'):
#     print('It starts with Hello')

# if not str.startswith('Python'):
#     print('It does not start with Hello')

# print(str.startswith('Hello'))
# print(str.startswith('Python'))

# #7.endswith ->검색 범위 지정가능

# if str.endswith('Python!'):
#     print('It ends with Python!')

# print(str.endswith('Python!'))

# str = "this is string example....wow!!!"

# print(len(str))
# suffix = "wow!!!"
# print(str.endswith(suffix))
# print(str.endswith(suffix,20))

# suffix ="is"
# print(str.endswith(suffix,2,4))
# print(str.endswith(suffix,2,6))

#8.index,rindex

# a = [123,421,212,11,24,102,29,92,10]
# print(a.index(212)) 

# nums_list = [1,2,3,3,3,5,6,8,9]
# nums_tuple = (1,2,3,3,3,5,6,8,9)
# nums_set = {1,2,3,5,6,8,9}

# print(nums_list.index(2)) #1
# print(nums_list.index(3)) #2
# #찾고자 하는 값이 여러개면 가장 작은 값을 반환

# print(nums_tuple.index(2)) #1
# print(nums_tuple.index(3)) #2

"""
set은 index 사용불가
print(nums_set.index(2)) #1
print(nums_set.index(3)) #2
"""


text = 'Welcome to Codetorial'

pos_Code_last = text.rindex('Code')
print(pos_Code_last)

"""
지정된 문자열이 없으면 에러처리코드(Exception)을 반환하는 rfind에 비해
rindex는 없기때문에 프로그램 실행시 오류가 발생함
pos_code_last = text.rindex('code')
print(pos_code_last)
"""