# # 2058. 자릿수 더하기
N = input()
result = 0
for i in range(len(N)):
    result = int(N[i:i+1]) + result
print(result) 

# 2056. 연월일 달력
T = int(input())
for i in range(T):
    test_case = input()
    result = list(map(str, test_case))
    result.insert(4,'/')
    result.insert(7,'/')
    result_1 = ''.join(result)
    if int(test_case[4:6]) < 1 or int(test_case[4:6]) > 12:
        result_1 = -1
    else:
        if int(test_case[4:6]) == 1 and\
            int(test_case[4:6]) == 3 and\
            int(test_case[4:6]) == 5 and\
            int(test_case[4:6]) == 7 and\
            int(test_case[4:6]) == 8 and\
            int(test_case[4:6]) == 10 and\
            int(test_case[4:6]) == 12:
            if int(test_case[7:]) > 31 or int(test_case[7:]) <1:
                result_1 = -1
        elif int(test_case[4:6]) == 4 and\
            int(test_case[4:6]) == 6 and\
            int(test_case[4:6]) == 9 and\
            int(test_case[4:6]) == 11:
            if int(test_case[7:]) > 30 or int(test_case[7:]) <1:
                result_1 = -1
        else:
            if int(test_case[7:]) > 28 or int(test_case[7:]) <1:
                result_1 = -1
    print(f"#{i+1} {result_1}")

# 2050. 알파벳을 숫자로 변환

alphabet = list(map(str, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
a = list(map(str, range(1,27)))
N = list(map(str, input()))

# for j in range(len(N)):
    for k in range(len(a)):
        if N[j] == alphabet[k]:
            N[j] = a[k]


# print(' '.join(N))

# 2047. 신문 헤드라인
headline = input()
print(headline.upper())

# 2046. 스탬프 찍기
n = int(input())
for i in range(n):
    print('#',end='')

# 2043. 서랍의 비밀번호
password = list(map(int, input().split(' ')))
print(abs(password[0]-password[1])+1)

# 2029. 몫과 나머지 출력하기 
T = int(input())
for i in range(T):
    a, b = map(int, input().split(' '))
    result_1 = int(a/b)
    result_2 = a%b
    print(f'#{i+1} {result_1} {result_2}')

# 2025. N줄덧셈
n = int(input())
result = 0
for i in range(1, n+1):
    result = i +result
print(result)

# 1938. 아주 간단한 계산기
a, b = map(int, input().split(' '))
print(f'{a+b}\n{a-b}\n{a*b}\n{a//b}')

#1933. 간단한 N 의 약수
N = int(input())
for i in range(1,N+1):
    if N % i == 0:
        print(i, end=' ')

# 1936. 1대1 가위바위보 D1
a, b = tuple(input().split(' '))
if (a, b) == (1, 3) or (a, b) == (2, 1) or (a, b == 3, 2):
    print('A')
elif (a, b) == (3, 1) or (a, b) == (1, 2) or (a, b == 2, 3):
    print('B')

# 2019. 더블더블
n = int(input())
for i in range(0, n+1):
    print(f"{2**i}", end=' ')

# 1545. 거꾸로 출력해 보아요
N = int(input())
for i in range(N, -1, -1):
    print(f"{i}", end=' ')