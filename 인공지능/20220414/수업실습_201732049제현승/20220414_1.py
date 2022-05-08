# f = open("newfile.txt",'w') # 경로 표시 안하면 소스파일과 같은 위차에 생성됨 -특정 위치를 원하면 특정 위치까지의 거리를 나타내주어야 한다.
# f.close()


#t-텍스트 모드로 파일 open, b-이진파일 읽어들임
# f = open("newfile.txt",'x') #파일이 있으면 실행시 에러
# f.close()
 
# f = open("ex_memo.txt",'w') # 경로 표시 안하면 소스파일과 같은 위차에 생성됨 -특정 위치를 원하면 특정 위치까지의 거리를 나타내주어야 한다.
# students = ['김철수', '최영', '한석규', '김석규']

# for student in students:
#      msg = student
#      f.write(msg+'\n')
# f.close()

# #file = open("hello.txt",'w')
# file = open("hello.txt",'wt') #텍스트 모드
# file.write('Hello World!')
# file.close()

# f = open('test.txt', 'a', encoding='UTF-8')#a:실행할 때 마다 계속해서 뒤에 내용 추가, w는 새로 실행한 내용으로 덮어씀(추가되지 않음)


# for i in range(4,10):
#      data ="%d 번째 줄입니다. \n"%i
#      f.write(data)
# f.close()

# dict1 = {'hello' : 1 , 'brother' : 2}
# file1 = open("Original.txt", "w")

# str1 = repr(dict1) #변수를 문자열로 변환
# file1.write("dict1 = "+str1+"\n")

# file1.close()

# test_file = open("test.txt","w")

# a = 1
# b = 2

# test_file.write('%d + %d = %d' %(a,b,a+b)+"\n")
# test_file.write('%d + %d = %d' %(a,b,a-b))

# test_file.close()

# from random import randint

# with open('text2.txt', 'w') as f:
#      f.write('이번주 로또 번호는 ->')
#      for lotto in range(6):
#           f.write(str(randint(0,50))+', ')

# #with는 close 필요 없음

# lines = ['안녕하세요. \n', '파이썬\n', '코딩 도장 입니다.\n']

# with open('hello2.txt', 'w')as file:
#      #file.writelines(lines)
#      #주석친 부분과 실행결과는 같음 , .writelines의 다른 표현
#      for msg in lines:
#           file.write(msg)
#           print(msg+'\n')

# file.close()

# f= open("hz.txt", "a", encoding='UTF-8')
# f.writelines(["\n홈짱닷컴", "\nHommzzang.com"])

# f.close()

f = open('ex_memo1.txt','w')
students = ['김철수', '최영', '한석규', '김태희']
for student in students:
     msg = student 
     f.write(msg + " ")

f.close()

f = open('ex_memo2.txt','w')
students = ['김철수', '최영', '한석규', '김태희']
f.writelines('\n'.join(students)) #위에는 한줄로 다나오지만 , 이건 한줄에 한개 씩 나옴 

f.close()
