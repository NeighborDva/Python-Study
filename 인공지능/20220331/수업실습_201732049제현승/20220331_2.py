# strip(), lstrip(), rstrip() ->원하는 문자열 제거 설정시 해당 문자열로 시작해야 삭제함
from cgitb import text
from cmath import pi
from dataclasses import replace


a= ' test'
#a= ' test '
#a= ' test !'

b= '~~.test.~~'
c= '~test!'

#print(a.lstrip())
#print(a.rstrip())
#print(a.strip())
#print(a.rstrip(), end =".")
# print(a.lstrip('t'))
# print(b.lstrip('t'))
# print(c.lstrip('t'))

# print(a.rstrip('t'))
# print(b.rstrip('t'))
# print(c.rstrip('t'))

# print(a.lstrip('~'))
# print(b.lstrip('~'))
# print(c.lstrip('~'))

# print(a.rstrip('~'))
# print(b.rstrip('~'))
# print(c.rstrip('~'))

# print(b.strip("~"))
# print(c.strip('~!'))

# text = '0000000Water boils at 100 degrees 000'
# print(text.lstrip('0'))
# print(text.rstrip('0'))
# print(text.strip('0'))

# text = ',,,,,123.....water....pp'
# # 여러문자 제거 -> 요거로 시작해야 해당 문자 제거는 단일 문자와 동일
# print(text.lstrip(',123.p'))
# print(text.rstrip(',123.p'))
# print(text.strip(',123.p'))

# text = ' Water boils at 100 degrees '

# print('[' + text.rstrip()+ ']')
# print('[' + text.lstrip()+ ']')
# print('[' + text.strip()+ ']')

#isspace()-문자열이 모두 공백이면 true반환

# txt = "  Hz  "

# x = txt.isspace()

# print(x) #false

# sentence = input("문자열을 입력하세요: ")
# table = {"알파벳" : 0 , "숫자": 0, "빈칸" : 0}

# for i in sentence:
#     if(i.isalpha()):
#         table["알파벳"] += 1
#     elif(i.isdigit()):
#         table["숫자"] +=1
#     elif(i.isspace()):
#         table["빈칸"] +=1
# print(table)

#ljust(), center(),rjust() -> 좌, 중앙, 우측 정렬 문자열 총 자리 정해주고 빈칸은 공백으로 채워 넣기
# s= '가나다라'
# n=7
# answer = ''
# for i in range(n-len(s)):
#     answer+=' '

# answer += s
# print(answer)

# print(s.ljust(n)) #좌측정렬
# print(s.center(n)) #중앙정렬
# print(s.rjust(n)) #우측정렬

a = "abc"
print(a.rjust(10))
print(a.rjust(10,'#'))
b = "def"
print(a.ljust(15))
print(a.ljust(15,'k'))


#split() -> 문자열을 일정한 규칙으로 잘라서 리스트로 생성
# s = "a b c d e f g"
# print(f's         : {s}')
 
# r = s.split()
# print(f's.split() : {r}')

# s = "aa.bb.cc.dd.ee.ff.gg"
# print(f's                : {s}')
 
# r0 = s.split()
# #r1 = s.split('.') #문장에있는 문자로 split 실시하여야함
# r1 = s.split('.',3)
# r2 = s.split(sep='.', maxsplit=3) #maxsplit ? ->몇개만 나누고 나머지는 다 묶어서 처리
# r2 = s.split('.', maxsplit=3)

# print(f"s.split()        : {r0}")
# print(f"s.split('.')     : {r1}")
# print(f"s.split(sep='.') : {r2}")



# #replace() ->대체

# text = '123,456,789,999'

# replaceAll = text.replace(",","!")
# replace_t1 = text.replace(",","!",1)
# replace_t2 = text.replace(",","!",2) #왼쪽부터 지정한 개수부터
# replace_t3 = text.replace(",","!",3)

# print("결과: ")
# print(replaceAll)
# print(replace_t1)
# print(replace_t2)
# print(replace_t3)

# #splitlines()->줄바꿈 기호 기준으로 쪼개기;

# txt = "홈짱닷컴\nHomzzang.com"

# x = txt.splitlines(True)

# print(x)

# g = 'Milk\nChicken\r\nBread\rbutter'
# print(g.splitlines())
# print(g.splitlines(True))

# g= 'Milk Chicken Bread Butter'
# print(g.splitlines(True))

# #join() -매개변수로 들어온 요소들을 하나의 요소로 만듬

# a = ['a', 'b', 'c', 'd', '1', '2', '3']
# print(a)
# print()
 
# # 리스트를 문자열로 : join 이용
# result1 = "".join(a)
# print(result1)
 
 
# # 리스트를 문자열로 : 하나하나 문자열을 더해서.
# result2 = ''
# for v in a:
#     result2 += v
 
# print(result2)

# #zfill() - 문자열 앞 0으로 채우기, 매개변수는 문자열의 총자리수를 의미 자리가 다 채워지면 0으로 안채워짐
# print( "3".zfill(3) )
# print( "s".zfill(4) )

# for x in range(3):
#     print(x)
#     print( str(x).zfill(4) )

# str = '1234'
# str_zero = str.zfill(8)
# print(str_zero)
