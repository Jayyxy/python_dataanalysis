# 학생 정보 리스트를 정의하세요.
students = [ ]

# 학생 정보를 추가
def add_student(name, age, grade) :
    students.append({'name': name, 'age': age, 'grade': grade})
   
#모든 학생 정보를 출력
def get_all_students(): 
    print("전체 학생 목록")
    for item in students :
        print(item)


# 이름으로 학생을 검색 후, 학생 정보 딕셔너리 반환
'''
- 'name' : key
- 리스트내에 있는 딕셔너리를 검색 : for 문 -> if문 -> return or print 
'''

def find_student(name): 
    for student in students : 
        if student['name'] == name :
            print(f'학생검색: {name}')
            print(student)
            


#  학생들의 평균 나이를 계산후, 반환
def dget_average_age():
    
    sum_age = 0
    
    for student in students :
        sum_age += student['age']

    age_avg = sum_age/len(students)
    
    return age_avg
