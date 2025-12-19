'''
조건문(if문)

'''
# Example
## 반지름으로 넓이 둘레 구하기 
radius = int(input("반지름을 입력하세요: "))

if radius > 0 :
    print('넓이 =', (3.14*radius**2))
    print('둘레 =', (2*3.14*radius))


## 정수를 입력하여 짝수 홀수 출력하기 
num1 = int(input('정수를 입력하세요: '))

if num1 % 2 ==0 :
    print(num1,'은 짝수입니다.')
else :
    print(num1,'은 홀수입니다.')




# if~else문 


## 정수를 입력하여 짝수 홀수 출력하기 
num2 = int(input('정수를 입력하세요: '))

if num2 % 2 ==0:
    print(num2,'은 짝수입니다.')
else:
    print(num2,'은 홀수입니다.')



# if~elif~else문
# 여러 개의 조건을 걸고 싶을 때는 ?
grade = input('점수를 입력해주세요: ')

if grade =='A':
    print('A등급입니다.')
elif grade =='B':
    print('B등급입니다.')
elif grade == 'C':
    print('C등급입니다.')
elif grade == 'D':
    print('D등급입니다.')
else:
    print('F등급입니다.') 

# 중첩 if문 
num1 = 10
num2 = -10

if num1 > 0 :
    if num2 > 0 :
        print('둘다 양수입니다.')
    elif num2 < 0 :
        print('num1은 양수 num1은 음수입니다.')
if num1 < 0 :
    if num2 > 0 :
        print('num1은 음수 num2는 양수입니다.')
    elif num2 < 0 :
        print('둘다 음수입니다.')


# 비교 연산자 체이닝

## Example1. H가 있는경우 H를 제거
a = ["H","H","h","E","F","s","d"]

if 'H' in a :
    a.remove('H')
    print('H를 제거하였습니다.')
else:
    print('H가 없습니다.')

## Example1. 길이가 5개인경우 2번 반복

word = 'python'

if len(word) >= 5 :
    print(word*2)

else :
    print(word)

## Example2. 단어를 입력할때 길이가 5이상이고 P로 시작한다면 출력

if len(word) >= 5 and 'P' in word :
    print(word)
else :
    print('조건에 맞지않는 단어 입니다.')

## Example2. 시험점수가 70이상 출석점수가 90이상이면 통과 시험점수가 통과이지만 출석점수가 90 미만이면 조건부 통과
## 둘다 충족못하면 미흡 출력    

score = int(input("시험 점수를 입력하세요: "))
attendance = int(input("출석 점수를 입력하세요: "))

if score >= 70 and attendance >= 90:
    print('통과')
elif score >= 70 and attendance < 90:
    print('조건부 통과(출석 미달)')
else:
    print("미흡")
