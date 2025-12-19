
'''

시퀀스 자료형 : 순서가 있으며, 여러 원소를 담고 있는 자료형

Index : 시퀀스 자료형의 원소의 위치 , 첫번째 위치는 0 부터 시작 

'''



''' 
(1) 인덱싱(Indexing) : 값 읽기 

문자열/리스트[인덱스_번호]

'''

alpha = [1,3,5,7,9]
print(alpha[2]) #3번째 위치 원소 가져옴

beta = "Hello Python"
print(beta[4]) #5번째 글자 가져옴



''' 
(1) 인덱싱(Indexing) : 값 수정하기 


리스트[인덱스_번호] = 값 

** 문자열은 수정이 불가능 (lmmutable 타입)

'''

num_list = [1,2,3,4,5]
num_list[1] = 20
num_list[4] = 50

print(num_list)


''' 
(2)슬라이싱(Slicing)


문자열/리스트[시작 인덱스 : 끝 인덱스]


'''
num_list= [1,2,3,4,5]
print(num_list[1:4]) # 인덱스 1부터 4미만의 원소 가져오기

str_var = "Hi! Python"
print(str_var[0:3]) # 인덱스 0부터 3미만의 원소 가져오기 




''' 
(3)인덱싱(Indexing)과 슬라이싱(Slicing) 확장 


음수의 인덱싱, 시작 범위 또는 끝 범위를 비울 수 있음

* 음수 인덱싱 : 파이썬 한정 
* 원소 읽는 방향은 순차적으로 

'''

# python 은 마이너스 인덱스를 사용할수 있다. 
a = "Hello World"
b = [4,5,3,2,1]
c = [4,5,6,1,2,3,4]
print(a[-2:])  # ld 
print(b[1:-3])  # 5 
print(c[5:-4])



''' 
시퀀스 자료형 활용 : in 연산자

원소 in 시퀀스 자료형

''' 
## true/false로 반환 
str_var = "Dada dd ad"
print("Dad" in str_var)
print("DaD" in str_var)

list1 = [10,4,7,6,1,2]
print(20 in list1)


''' 
시퀀스 자료형 활용 : len()함수

len(시퀀스 자료형)

자료형의 길이(=총 원소의 개수)를 구하는 함수 
''' 

num_list = [1,2,3,4,5]
word = "Python"


print(len(num_list))
print(len(word))


