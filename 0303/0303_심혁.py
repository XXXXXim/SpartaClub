T = int(input())
for tc in range(1,T+1):
    N= int(input())
    #0은 통로, 1은 벽, 2는 괴물.
    #격자생성
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    
    count = 0
    number = 0
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 0:
                count += 1
            elif grid[r][c] == 2:
                for d in range(4):
                    for k in range(1,N):
                        nr = r + dr[d]*k
                        nc = c + dc[d]*k
                        if 0 <= nr < N and 0 <= nc < N:
                            if grid[nr][nc] == 0:
                                number += 1
                            if grid[nr][nc] == 1:
                                break
                            if grid[nr][nc] == 2:
                                pass
    print(f"#{tc} {count- number}")