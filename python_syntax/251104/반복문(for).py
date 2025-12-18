total = 0 
seq = [1,3,5,7,9]

for i in seq :
    print(f'현재 원소 :{i}') 
    total +=1 
print(f'최종 결과 : {total}') #종속되지 않음 

total_2 = 0 # 초기화는 필수 
for i in seq :
    print(f'현재 원소 2씩 늘리기 :{i}')
    total_2 +=2 
print(f'2씩 늘린 최종결과 : {total_2}')



# Example1 . 가격목록의 할일율을 적용한 가격 출력 (10%)

price = [1000, 300400, 30000,5300, 15000]
discount_radio = 0.9

for i in price :
    print(f'할인한 가격 {price+discount_radio}')



## for ~ range 
## a부터 b-1까지 숫자 생성
for i in range(5,10,2): # b-a 번 반족 
    print(i)
print("----------------") 
for i in range(5) : # 0부터 5미만 
    print(i)

# range() + len() 방식 : 인덱싱을 통해서 가져옴 

## 문자열로 반복문

str_var = "Hello world"

for i in range(len(str_var)):
    ## 문자열의 길이는 12 : 0부터 11까지 
    print(i, str_var[i])

# Example 1. 상품의 개수 만큼 가격 합하기

price = [20000, 15000, 25000, 50000]
quantities = [3,4,5,2]

total = 0
for i in range(len(price)) : 
    total += price[i] * quantities[i]
    print (f'총 구매액 : {total}')


# 상품 가격이 10,000원 이상인 상품에 대하여 10% 할인 적용한 가격 리스트 출력 
prices = [4000 , 5000,6000, 10000, 3000]
discounted = []

for i in range(len(prices)) : 
    if prices[i] >= 10000 :
        discounted.append(prices[i]*0.9)
    else : 
        discounted.append(prices[i])

print(discounted)