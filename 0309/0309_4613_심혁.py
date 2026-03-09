T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    arr = [input() for _ in range(N)]
    
    #최소비용 = 모든 값을 다 새로 칠해야하는 최악의 경우 +1로 가정(가장큰)
    min_cost = N*M+1
    
    for i in range(N-2):
        for j in range(i+1, N-1):
            #이번 구역분할에서 새로 칠해야하는 총비용
            cost = 0
            #흰색칠
            for w in range(0,i+1):
                #M(전체 칸수) - 현재 줄에 이미칠해진 'W'수 = 새로 칠해야 할 칸수
                cost += M - arr[w].count('W')
            #파랑칠    
            for b in range(i+1, j+1):
                cost += M-arr[b].count('B')
            #빨강칠
            for r in range(j+1, N):
                cost += M - arr[r].count('R')
                
            #최솟값갱신
            if min_cost > cost:
                min_cost = cost
                
    print(f"#{tc} {min_cost}")