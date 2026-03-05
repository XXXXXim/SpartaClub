T=int(input())
for tc in range(1,T+1):
    N,M = int(input().split())

    grid = list(int(input().split())for _ in range(N))

    #파리를 잡는거에여
    #각 방향으로 M칸 파리 잡을수있음(중삼포함 뿌려지는 칸수)
    # '+' or 'x' 둘중하나임.

    #case 1: + 경우
    # 십자가 델타설정
    dr1=[-1,1,0,0]
    dc1=[0,0,-1,1]
    #최대 파리 수
    max_flies = 0
    #중심점 돌아가면서 (완전탐색)
    for r in range(N):
        for c in range(N):
            
            sum_1 = grid[r][c] # +모양으로 잡은 파리 수
            #4방향 탐색
            for d in range(4):
                #스프레이 파워 M에 맞춰 1부터 M-1까지 뻗어나감
                for step in range(1,M-1):
                    nr1= r+dr1[d]*step
                    nc1= c+dc1[d]*step
                    #범위안에 있으면 파리수더하기
                    if 0<nr1<N and 0<=nc1<N:
                        sum_1 += grid[nr1][nc1]