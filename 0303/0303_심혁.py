T = int(input())
for tc in range(1,T+1):
    N= int(input())
    #0은 통로, 1은 벽, 2는 괴물.
    #격자생성 N x N 
    grid = [list(map(int, input().split())) for _ in range(N)]
    # 십자이동 가능하므로 델타입력
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    #0인 통로의 개수 count
    count = 0
    #괴물주변 0인 통로의 개수 number
    number = 0
    #전범위 탐색하면서 0인 통로의 개수 세고, 2인 괴물주변의 0인 통로의 개수 세기
    for r in range(N):
        for c in range(N):
            # 통로면 count 하나 올리기
            if grid[r][c] == 0:
                count += 1
            # 괴물이면 4방향 탐색하면서 0인 통로의 개수 세기
            elif grid[r][c] == 2:
                for d in range(4):
                    #갈 수 있는 최대 길이 k
                    for k in range(1,N):
                        # nr,nc는 괴물에서 d방향으로 k만큼 떨어진 위치
                        nr = r + dr[d]*k
                        nc = c + dc[d]*k
                        #범위안에 있고, 0인 통로면 number하나 올리고, -1로 바꿔서 중복세지않게하기
                        if 0 <= nr < N and 0 <= nc < N:
                            if grid[nr][nc] == 0:
                                number += 1
                                grid[nr][nc] = -1
                            # 괴물주변의 0인 통로는 세지만, 벽이나 괴물은 세지않고,
                            # 벽이나 괴물이 나오면 그 방향으로는 더이상 탐색하지않기
                            elif grid[nr][nc] == -1 or grid[nr][nc] == 2:
                                pass
                            elif grid[nr][nc] == 1:
                                break
                        #범위를 벗어나면 그 방향으로는 더이상 탐색하지않기    
                        else:
                            break
    print(f"#{tc} {count- number}")
