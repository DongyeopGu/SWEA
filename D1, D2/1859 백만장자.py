T = int(input())        # 테스트 케이스 입력
for i in range(T):      # 테스트 케이스 만큼 반복 
    N = int(input())    # 매매가 개수 입력
    a = list(map(int, input().split(' ')))  #매매가 입력
    b = 0               # 비교해서 값 바꾸는용
    c = 0               # 결과값 저장용
    for j in a[::-1]:   # 매매가 입력을 뒤에서 부터 가져와서 반복
        if j > b:       # 뒤가 앞보다 큰경우
            b = j       # b를 맨 뒤 값으로 초기화 후 앞에 있는 값이 뒤보다 클때 다시 값 변경
        c += b-j        # 이득 계속 저장
    print(f'#{i+1} {c}')    # 출력
    