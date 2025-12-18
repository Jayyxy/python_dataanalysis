# 할당하기
var1 = 31
var2 = "Hello" 

print(var1)
print(var2)

# 연산하기 
## 몫
print(15//4)
## 나머지  
print(5%3)
## 제곱 
print(3**3) 

# 형변환
num1 = int(input())
num2 = int(input())

print(type(num1))
print(type(num2))
print(type(num1+num2))


# 명제 
## and : 모든 연산자가 참이여야만함 
print (0 >= 0 and 2!= 4)

## or : 하나라도 '참'이면 참이다 
print (0==0 or not (0>0))
print (not (5))


print("ABCD" == "abcd") # 대소문자 구분 
print("ABCD" == "abcd" or 10 != 11) 

# 연산순서 

## (3+4) -> (7) *2 -> 14 > 10  
result = (3+4) * 2 >10 

## (a*b) -> 10 > 8 -> c//b -> 5==5 -> true and true  
a=5
b=2
c=10

result = (a*b > 8) and (c//b==5)
print (result)