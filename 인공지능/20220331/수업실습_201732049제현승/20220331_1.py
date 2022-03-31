#isalnum()

# text1 = "네이스123" 
# text2 = "123123" 
# text3 = "!@#$" 
# text4 = "!@#$1234" 
# text5 = "wtf" 
# text6 = "wtf123123" 
# print(text1.isalnum()) 
# print(text2.isalnum()) 
# print(text3.isalnum()) 
# print(text4.isalnum()) 
# print(text5.isalnum()) 
# print(text6.isalnum())

#isalpha()

# text = "!#$$!@$!!!!!!!!@$#231421234네123^&^#$#이!#12313_+{스"
# text1 = "네이스" 
# text2 = "123123" 
# text3 = "!@#$" 
# check = "" 
# print(text1.isalpha()) 
# print(text2.isalpha()) 
# print(text3.isalpha()) 
# for i in text: 
#     if i.isalpha(): 
#         check += i 
        
# print(check)

# a = "BlockDMask" # 문자로만 이루어짐 
# b = "1234Blog" # 문자 + 숫자 
# c = "131231" # 숫자 
# d = "-234" # 음수 
# e = "1.23" # 소수점 
# f = "3²" # 3의 2제곱 기호 숫자 
# g = "⅔" # 수학 기호 숫자 2/3 
# h = "0" # 0 
# i = "0123" # 0 으로 시작한 숫자 # 

# #isdigit()-문자열이 숫자로 이루어져 있는지 판별, 실수나 음수는 판별 불가
# str.isdigit("문자열") 
# print(f"str.isdigit('{a}') : {str.isdigit(a)}") 
# print(f"str.isdigit('{b}') : {str.isdigit(b)}") 
# print(f"str.isdigit('{c}') : {str.isdigit(c)}") 
# print(f"str.isdigit('{d}') : {str.isdigit(d)}") 
# print(f"str.isdigit('{e}') : {str.isdigit(e)}") 
# print(f"str.isdigit('{f}') : {str.isdigit(f)}") 
# print(f"str.isdigit('{g}') : {str.isdigit(g)}") 
# print(f"str.isdigit('{h}') : {str.isdigit(h)}") 
# print(f"str.isdigit('{i}') : {str.isdigit(i)}") 
# print() 

# # "문자열".isdigit() 
# print(f"'{a}'.isdigit() : {a.isdigit()}") 
# print(f"'{b}'.isdigit() : {b.isdigit()}") 
# print(f"'{c}'.isdigit() : {c.isdigit()}") 
# print(f"'{d}'.isdigit() : {d.isdigit()}") 
# print(f"'{e}'.isdigit() : {e.isdigit()}") 
# print(f"'{f}'.isdigit() : {f.isdigit()}") 
# print(f"'{g}'.isdigit() : {g.isdigit()}") 
# print(f"'{h}'.isdigit() : {h.isdigit()}") 
# print(f"'{i}'.isdigit() : {i.isdigit()}")



#isdecimal()- 해당 문자열이 0~9 숫자로 이루어져 있는지 검사

#isnumeric -  수로 볼 수 있는 것인 경우 True를 반환

# a = '12345678' 
# print(a.isdigit()) 
# print(a.isdecimal()) 
# print(a.isnumeric())

# x = '3²'
# print(x)
# print(x.isdigit()) 
# print(x.isdecimal()) 
# print(x.isnumeric())

#upper(), lower(), islower(), isupper()
# a = "I Love Python"

# print(a.islower()) #소문자인가?
# print(a.isupper()) #대문자인가?
# print(a.upper()) #대문자로 변환
# print(a.lower()) #소문자로 변환

# str = "This is string example... wow!!!"
# print(str.islower())
# print(str.isupper())

# str = "this is string example... wow!!!"
# print(str.islower())

#swapcase - 소문자-> 대문자, 대문자->소문자(알파벳만)

# str = "this is string example... wow!!!"
# print(str.swapcase())

# str = "THIS IS STRING EXAMPLE...WOW!!!"
# print(str.swapcase())

#istitle()- 문자열이 title 스타일(단어가 대문자 + 소문자 구성)인경우 판단
# str = "This Is String Example...Wow!!!"
# print(str.istitle())

# str = "This is string example....wow!!!"
# print(str.istitle())

#title()- 문자열 단어 앞만 대문자로 변환

# str = "This is string example...wow!!!"
# print(str.title())

#capitalize() - 문자열의 첫글자는 대문자, 나머지 소문자

print('hello world!'.capitalize()) #Hello world!
print('HELLO WORLD!'.capitalize()) #Hello world!