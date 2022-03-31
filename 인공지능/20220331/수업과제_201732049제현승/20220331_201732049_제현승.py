#1
print("#1")

price_list = [32100,32150,32000,32500]

for i in range(4):
    print(i,end=" ")
    print(price_list[i])

print()

#2
print("#2")
for i in range(100,121,10):
    print(i,end=" ")
    print(price_list[(int)(i/10)-9])

print()

#3
print("#3")
for i in range(2002,2051,4):
    print(i)
print()

#4
print("#4")
for i in range(10):
    print(i/10)
print()

#5
print("#5")
ticker = "btc_krw"
ticker_upper = ticker.upper()
print(ticker_upper)
print()

#6
print("#6")
file_name = "보고서.xlsx"
if(file_name.endswith("xlsx")):
    print("파일 이름이 'xlsx'로 끝납니다.")
else:
    print("파일 이름이 'xlsx'로 끝나지 않습니다.")
print()
#7
print("#7")
a="hello world"
a_split = a.split() #기본값 공백
print(a_split)
print()

#8
print("#8")
date = "2020-05-01"
date_split = date.split('-')
print(date_split)
print()

#9
print("#9")
stock = "5,969,782,550"
stock_replace = stock.replace(',','')
stock_num = int(stock_replace)

print(f"{type(stock_num)}형 stock_num의 값은 {stock_num}입니다.")

print()

#10
print("#10")
a="hello world"
a_split = a.split() #기본값 공백
print(a_split)
print()

#11
print("#11")
price = ['20180728', 100, 130, 140, 150, 160, 170]
price_slice = price[1:7]
print(price_slice)
print()

#12
print("#12")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums_slice = nums[1::2]
print(nums_slice)
print()

#13
print("#13")
list = [3,100,23,44]
for i in list:
    if(i % 3 ==0):
        print(i)

