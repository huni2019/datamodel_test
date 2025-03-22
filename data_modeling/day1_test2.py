n = int(input("정수를 입력하시오: "))
fact = 1  #초기값

# 반복적으로 정수를 곱한다. 이 정수는 1부터 n까지 1씩 증가함
for i in range(1, n+1):
    fact = fact * i

print(f"{n}!은 {fact}입니다.")