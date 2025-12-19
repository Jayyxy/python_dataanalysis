 
# 여러 함수, 변수, 클래스 등을 하나의 파일에 묶어 놓는 경우 
#   -> 프로젝트 규모가 커짐에 따라 코드 양 증가 
#   -> 수정시 기능 찾기 어려움, 유지보수 불편, 재사용 어려움 


# 모듈(Module)
# : 여러 함수, 변수, 클래스 등을 하나의 파일로 묶어 놓는 것
# -> 특정 기능(주제) 마다 모듈을 분리, 유지보수와 재사용에 용이


# 모듈의 종류 
# -> 내장 모듈/ 사용자 정의 모듈 


# 모듈 불러오기
# : 모듈을 불러온 뒤 모듈에 있는 기능(함수, 변수, 클래스) 사용하기 
import random # 내장 모듈

print(random.randrange(0,2))

# 내장 모듈(Built-in) - math 모듈
import math 

print(math.pi) # 원주율
print(math.e) # 자연상수
print(math.sqrt(16)) # 제곱근
print(math.pow(2,3)) # 거듭제곱
print(math.ceil(3.1)) # 올림
print(math.floor(3.9)) # 내림 


