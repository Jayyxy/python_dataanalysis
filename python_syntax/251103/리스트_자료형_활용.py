
''' 
중첩 리스트 (Nest List) 
''' 
# 
### [1,2,3]
### [4,5,6]
### [7,8,9]

nested = [[1,2,3],[4,5,6],[7,8,9]]

print(nested[0][1])
print(nested[0]) 

nested_list = [ 
    ["a","c","f"],
    ["g","e","e"],
    ["d","e"] 
    ]


'''
리스트의 다양한 메서드 (리스트_변수.메서드())

 • .append(x) :  원소 x 를 가장 마지막에 추가 
 • .insert(i, x) : i번째 위치에 원소 x 추가 
 • .remove(x) : 리스트에 처음 검색된 원소 x 삭제 
 • .pop(i) : i번째 인덱스의 원소를 삭제후 반환 (원소 빼내기)
 • .sort() : 정렬, 기본은 오름차순
 • .index(x) : 원소 x에 해당하는 인덱스 검색 
 • .count(x) : 원소 x 가 들어있는 개수 출력 
 • .clear() : 모두 제거

 

 *** remove(), pop(), index() 대상의 원소나 인덱스가 존재하지 않는 경우 에러 발생 
'''

a = [4,3,2,5,1]

## append  
a.append([3,4,5])
print(a) # [4, 3, 2, 5, 1, [3, 4, 5]]

## insert
a[-1].insert(0,2) 
print(a) # [4, 3, 2, 5, 1, [2, 3, 4, 5]]

num_list = [3,1,2,3]

## remove 
## 중복된 원소가 있는경우 처음 검색된 값을 삭제 
num_list.remove(3)
print(num_list) # [1, 2, 3]

## pop 
## 아무것도 없는 경우 마지막 원소를 대상으로 수행 
num_list=[1,2,3,4,5] 
print(num_list.pop(1)) # 2 
print(num_list.pop(1)) # 3
print(num_list.pop()) # 5  (마지막 원소)

num_list

# index 
num_list = [3,1,4,1,2]
print(num_list.index(4))
print(num_list.index(1)) # * 중복값 -> 맨처음 원소의 인덱스값 반환 

# count
# 리스트 내 해당 원소가 들어있는 개수 
num_list = [3,1,4,1,2,1,3]

print(num_list.count(1)) # 2
print(num_list.count(3)) # 1

a = ["a","b","a","A","B","c","d"]

print(a.count("a"))

# sort
# reverse=True : 내림차순 (기본값 : 오름차순 )
a.sort()
print(a)# ['A', 'B', 'a', 'a', 'b', 'c', 'd']

b = [4,5,9,7,5,2,1,6,3] # b.sort(reverse=True)
b.sort(reverse=True)
print(b)