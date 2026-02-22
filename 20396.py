T=int(input())

for tc in range(1,T+1):
    #N=돌의 개수, M=뒤집기 횟수
    N,M=map(int,input().split())
    #돌의 초기상태를 리스트로 저장
    #예: 0 1 0 1 0
    stones = list(map(int,input().split()))
    
    #M번의 뒤집기 연산 수행
    for _ in range(M):
        
        #i=시작위치(1번부터 시작)
        #j=뒤집을 돌의 개수
        i,j = map(int,input().split())
        
        #파이썬은 0번 인덱스부터 시작하므로
        #실제 리스트 인덱스로 변경
        start = i-1
        
        #뒤집을 마지막 위치 계산
        # i부터 j개 이므로 i+j-1
        # 하지만 범위를 벗어나면 안되므로 N과 비교
        end = min(N, i+j-1)
        #기준이 되는 색은 시작 돌의 색
        color = stones[start]
        # starts부터 end-1까지 모두 같은색으로 변경
        for k in range(start,end):
            stones[k] = color
    print(f'#{tc}', *stones)
