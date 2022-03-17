#20220317 과제

#1
print("Hello world")

#2
print("Mary's cometics")

#3
print("신씨가 소리질렀다. \"도둑이야\".")

#4
print('"C:\Windows"')

#5
print("안녕하세요.\n만나서\t\t반갑습니다.")
#\n은 줄바꿈, \t은 특정 칸만큼 띄어쓰기를 적용하여 출력되도록 합니다.

#6
movie_rank = ['닥터스트레인지', '스플릿', '럭키']
print(movie_rank)

#7
movie_rank.append('배트맨') #리스트의 맨뒤에 추가
print(movie_rank)

#8
movie_rank.insert(1,'수퍼맨') # 기존에 있던 값을 덮어씌우는게 아니라 뒤로 밀어냄
print(movie_rank)

#9 
num = [1,2,3,4,5]
sum =0
for i in num:
    sum+=i

print(sum)

#10
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지","라면", "팥빙수", "김치전"]
count = 0
for i in cook:
    count+=1

print("리스트에 저장된 데이터의 개수는 %d개 입니다." %count)

#11
num = [1,2,3,4,5]
sum =0
for i in num:
    sum+=i

avg = sum/len(num) #len->리스트의 평균을 의미

print(avg)

#12
print(3 == 5) #False

#13
print(3 < 5) #True

#14
x=4
print(1<x<5) #True

#15
print((3 == 3) and (4!=3)) #True


