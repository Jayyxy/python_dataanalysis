# Example 1. 계좌 잔액이 인출할 금액보다 작을 때까지 인출하는 반복문
balance = 10000 # 초기 금액 
withbance = 1500 # 인출금액 

while balance >= withbance :
    balance -= withbance
    print(f'{withbance}원 인출하였습니다.')
    print(f'현재 잔액 : {balance}')

print(f"인출종료, 최종잔액 {balance}")

numbers = [4,2,5,6,9,8,10,5]
target = 10 
i = 0 


while i < len(numbers):
    if numbers[i] == target:
        print(f"{i+1}번째에서 {target} 탐색 완료")
        break
    i+=1


if i == len(numbers):
    print("탐색하지 못하였습니다.")



tp = (4,2,1,5,6)
tp2 = (100,200)

print(tp[1])
print(tp[2:4])
print(6 in tp)
print(len(tp))
print(tp2 * 3)

tp.append(6)


a,b,c,d,e = input().split()
print(a,b,c,d,e)
print(type(a))

x,y,z = list(map(int, input().split()))
print(x,y,z)
print(type(x),type(y),type(z))

