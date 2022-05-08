# ## read 함수

# import io

# f = open('t2.txt','r',encoding='UTF-8') #메모장은 utf - 8로 작성했기 때문에 추가해주어야함, encoding = 추가않하면 에러 발생

# print("\n1.read()")
# print(f'위치: {f.tell()}')

# #read-하나씩 읽어오기
# s1  = f.read(1)
# print(s1)

# #readline() 한 라인씩

# print("\n2.readline()")
# print(f'위치: {f.tell()}')

# s2 = f.readline()

# #s1  = f.read(1)
# #print(s1)
# print(s2)

# #readlines()- 모두 읽어옴
# print("\n3.readlines()")
# print(f'위치: {f.tell()}')

# s3 = f.readlines()

# #s1  = f.read(1)
# #print(s1)
# print(s3)

#파일 r모드로 열기
f=open('test.txt','r', encoding='UTF-8')
line = f.readline() #파일의 라인 끝에 줄 바꿈 (\n)이 있을 경우 줄바꿈 포함
line = line.strip() #줄바꿈 문자 제거
print(line)
line = f.readline()
line = line.strip()
print(line) #2번째 라인 출력
line = f.readline()
line = line.strip()
print(line) #3번째 라인 출력
#파일의 맨앞으로 옮기기 -seek(), 0입력시 첫글자 부터
#ㅌf.seek(0)
line = f.readline()
line = line.strip()
print(line) #4번째 라인 출력

f.close()