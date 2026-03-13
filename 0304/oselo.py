T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())

    r, c, color = map(int, input().split())

    grid = [list(map(int, input().split())) for _ in range(N)]

    #흑돌
    b = 0
    #백돌
    w = 0
    #8방향 다 탐색
    dr = [-1,1,0,0,-1,-1,1,1]
    dc = [0,0,-1,1,-1,1,-1,1]
    # 돌 놓기
    while M:
        #돌찾기
        # 흑돌일 경우
        if color == 1:
            grid[r][c] == 1
            b +=1
            #8방향 탐색
            for d1 in range(8):
                #두칸 더 확인해보기
                for k1 in range(2):
                    nr1 = r + dr[d1]*k1
                    nc1 = c + dc[d1]*k1
                    #범위 벗어나지 않게 설정
                    if 0 <= nr1 < N and 0 <= nc1 < N:
                        #만약 범위내 칸이 흑돌도 아니고 백돌도 아니면
                        if grid [nr1][nc1] != 1 and grid[nr1][nc1] != 2:
                            # 공백이다
                            grid[nr1][nc1] = -1
                            # 만약 끝칸이 흑돌이고
                        if grid[nr1+1][nc1+1] == 1:
                                # 그 전 칸이 백돌이면
                            if grid[nr1][nc1] ==2:
                                #사이에 있는 칸은 흑돌이 된다
                                grid[nr1][nc1] == 1
                                b +=2
                            else:
                                break
        
        #백돌일 경우
        if color == 2:
            grid[r][c] == 2
            w +=1
            #8방향 탐색
            for d2 in range(8):
                #두칸 더 확인해보기
                for k2 in range(2):
                    nr2 = r + dr[d2]*k2
                    nc2 = c + dc[d2]*k2
                    #범위 벗어나지 않게 설정
                    if 0 <= nr2 < N and 0 <= nc2 < N:
                        #만약 범위내 칸이 흑돌도 아니고 백돌도 아니면
                        if grid [nr2][nc2] != 1 and grid[nr2][nc2] != 2:
                            # 공백이다
                            grid[nr2][nc2] = -1
                            # 만약 끝칸이 흑돌이고
                        if grid[nr2+1][nc2+1] == 1:
                                # 그 전 칸이 백돌이면
                            if grid[nr2][nc2] ==2:
                                #사이에 있는 칸은 흑돌이 된다
                                grid[nr2][nc2] == 1
                                w +=2
                            else:
                                break
                
    print(f'#{tc} {b} {w}')                  

