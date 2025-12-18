
# 함수(funciton)
# : 반복적으로 사용하는 여러 줄짜리 코드에 이름을 붙여서 저장 

# 함수의 종류 : 내장함수 / 사용자 정의 함수 



# 사칙연산 계산기 만들기 

def add(num1, num2):
    return num1 + num2

def sub(num1,num2):
    return num1-num2 

def mul(num1,num2) :
    return num1*num2

def div(num1,num2) :
    return num1 / num2 


print(add(3,5))
print(sub(10,7))
print(mul(4,6))
print(div(15,5))


# 디폴트 매개변수
# : 매개변수에 디폴트 값을 명시하는 것으로 매칭되는 인자 없이 호출 시 디폴트 값 사용 
def def_para(country = 'korea') :
    print('I am from', country)

print(def_para('India'))
print(def_para('Brazil'))
print(def_para)

# 가변 매개변수
# : 여러개의 값을 한 번에 받을 수 있는 매개변수(*args)
# 매개변수 이름 앞에 *을 붙여주면 가변 매개변수가 된다
# 전달 받은 매개변수는 Tuple 형태로 받은 값들을 묶는다 

kor, eng, mat, sci = 98, 77, 85,  90

def max_score(*args) :
    return max(args)

print(max_score(kor,eng,mat))
print(max_score(eng,mat,sci))


