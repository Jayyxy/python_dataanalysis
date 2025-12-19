# 딕셔너리 
person = {
    "name" : "Gildong",
    "age" : 30,
    "address" : "서울특별시 도봉구",
    "Phone_number" : "01023423333",
    "email" : "abc@acb.com"  
}


print(person["name"])
print(person["age"])
print(person["address"])



# 딕셔너리 자료 삭제하기
person = {"name" : "Gildong","age" : 25 ,"address" : "서울시 강남구"}

del person["age"]
print(person)



# Example 1. 딕셔너리  level에서 medium의 값을 가져오기
level = {'low' : 1 , 'medium' : 5}

level['medium']
# Example 1. 딕셔너리  level에서 low 키가 있는지 확인하기

'low' in level
# Example 1. 딕셔너리  level에 {'high' : 10} 쌍을 추가하기

level['high'] = 10 

# Example 1. 딕셔너리  'low' 키를 삭제하기 
del level['low']



# 데이터 모델

company = {
    "name" : "ABC Corp",
    "departments" : {
        "HR" : {
            "manager" : "이명희",
            "employees" : ["홍길동", "김민수"]

        },
        "IT" : {
            "manager" : "박지훈",
            "employees" : ["최수빈","정우성","이서연"]
        }
    }
}
print(company["departments"]["HR"]["manager"])


# Zip 함수 확장 
# 가장 짧은 길이의 리스트의 기준으로 길이에 맞춘다 

a = [1,2,3]
b = [10,20]
c = [100,200,300,400]

print(list(zip(a,b,c)))


title = ['name','age','year']
values= ['John',30,1996]

print(dict(zip(title,values)))

# names와 scores라는 각각 빈 리스트를 정의하고, 5명의 이름과 점수를 입력 받아 각 리스트에 저장 후,
# 이 두 개의 리스트를 활용하여 딕셔너리를 생성하시오 
names = []
scores = []

for i in range(5) :
    names.append(input("이름을 입력하세요"))
    scores.append(int(input("점수를 입력하세요")))

result= dict(zip(names, scores))
print(result)
