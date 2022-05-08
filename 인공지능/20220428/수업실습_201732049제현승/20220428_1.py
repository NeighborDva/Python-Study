#numpy, numpy는 과학 계산을 위한 라이브러리로서 다차원 배열을 처리하는데 필요한 여러 유용한 기능을 제공

from turtle import pensize
import numpy as np #패키지 로드하여 np로 사용
# a = [[1,2,3],[4,5,6]] #리스트에서 행렬 생성, 2차행렬
# b = np.array(a)
# print(b)

# print(b.ndim)#배열 열수
# print(b.shape)#배열 개수(행 열)
# print(b[0,0])
# print(b[0,1])

# print(np.zeros((2,2))) #영행렬 생성
# c =np.zeros((2,2))
# print(c)

# print(np.ones((3,3)))#유닛 행렬 생성 (1행렬)

# print(np.full((3,3),2)) #지정 숫자로 채워진 행렬 생성

# print(np.eye(3)) #단위행열(대각선 원소가 모두 1인 행렬), 지정 크기 * 지정크기 행렬 생성후 대각선 1로 초기화

# a= np.arange(20) #0~19 생성 1행, 20열
# print(a)

# b= a.reshape((4,5)) #4행 5열로 변경, 원래 배열의 사이즈에 맞게 변경사이즈 지정해야함
# print(b)

# lst = [
#      [1,2,3],
#      [4,5,6],
#      [7,8,9]
# ]
# arr = np.array(lst)
# a= arr[0:2,0:2]
# print(a)
# a= arr[1:,1:]
# print(a)
# a= arr[1:2,1:2]
# print(a)

# a= np.array([1,2,3])
# b= np.array([4,5,6])

# c= a+b #각요소 더하기
# #c= np.add(a,b)
# print(c)

# c= a-b #각요소 빼기
# #c= np.substract(a,b)
# print(c)

# c= a*b #각요소 곱하기
# #c=np.multiply(a,b)
# print(c)

# c= a/b #각요소 나누기
# #c = np.divide(a,b)
# print(c)

arr1 =[[1,2],[3,4]]
arr2 =[[5,6],[7,8]]
a = np.array(arr1)
b = np.array(arr2)

c= np.dot(a,b) #행렬 곱 실행, 요소 곱 아님 multiply랑 혼동 x
print(c)

a= np.array([[-1,2,3],[3,4,8]])
s= np.sum(a) #모든 원소의 합
#print(s)
print("sum=",a.sum())
print("sum by row=",a.sum(axis=0))#같은 열(axis=0 x축) 값 합, 같은행(axis=1 y축)값 합,어진 축에서 배열요소의 합을 반환

print("mean = ", a.mean())#평균
print("sd=",a.std()) #표준 편차
print("product =", a.prod(axis=0))#주어진 축에서 배열요소의 곱을 반환, 축 안주면 모든 요소의 곱 구함
