#20220324 과제

#1
print("1번")
letters = 'python'
print(f'첫번째: {letters[0]} 세번째: {letters[2]}')

print()
#2
print("2번")
string = "PYTHON"
str_len = len(string)

for i in range(str_len-1,-1,-1):
    print(string[i],end="")


print()
#3
print("3번")
url = "http://sharebook.kr"
url_len = len(url)
search_str = input("문자열 입력: ")
index = url.rfind(search_str)
if(index != -1):
    print(f'{search_str}의 index는 url[{index}]입니다.')
    print(url[index:url_len])
    #kr만 뽑아서 출력
    index = url.find("kr")    
    domain = url[index:index+2]
    print(domain)
else:
    print(f'"{search_str}"이 없습니다.')
"""
3번 잘못된 
url = input("문자열 입력: ")
index = url.rfind("kr")
if(index != -1):
    print(f'kr의 index는 url[{index}]입니다.')
    domain = url[index:index+2]
    print(domain)
else:
    print("kr이 없습니다.")
"""

print()
#4
print("4번")
file_name = "보고서.xlsx"

if(file_name.endswith("xlsx")):
    print("파일 이름이 xlsx로 끝납니다.")
else:
     print("파일 이름이 xlsx로 끝나지 않습니다.")


print()
#5
print("5번")
file_name = "2020_보고서.xlsx"

if(file_name.startswith("2020")):
    print("파일 이름이 2020으로 시작합니다.")
else:
     print("파일 이름이 2020으로 시작하지 않습니다.")


print()
#6
print("6번")
score = int(input("점수: "))

if(score>80):
    print("A학점")
elif(score>60):
    print("B학점")
elif(score>40):
    print("C학점")
elif(score>20):
    print("D학점")
else:
    print("E학점")


print()
#7
print("7번")
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지","라면", "팥빙수", "김치전"]
count = 0
for i in cook:
    count+=1

print("리스트에 저장된 데이터의 개수는 %d개 입니다." %count)


print()
#8
print("8번")
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
company = input('투자할 회사를 입력하시요. 입력: ')

warning = 0
for i in warn_investment_list:
    if(company == i):
        print("투자 경고 종목입니다.")
        warning = 1
        break

if(warning == 0):
    print("투자 경고 종목이 아닙니다.")


print()
#9
print("9번")
item_list = [100,200,300]
for i in item_list:
    i = i + 10
    print(i)


print()
#10
print("10번")
investment_list = ["SK하이닉스", "삼성전자", "LG전자"]

for i in investment_list:
    print(len(i))


