T = int(input())
for tc in range(1,T+1):
    #게임 맵의 높이가 H, 너비가 W
    H, W = map(int, input().split())
    #문자열 받는 격자생성
    grid = [list(input()) for _ in range(H)]
    #사용자가 넣을 입력의 개수를 나타내는 정수 N(0 < N ≤ 100)
    N = int(input())
    #길이가 N인 문자열
    moves = input()
    
    #델타 탐색 위한 방향 벡터 설정(상, 하, 좌, 우)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    tank = ['^', 'v', '<', '>'] #탱크의 방향을 나타내는 문자
   #
    for r in range(H):
        for c in range(W):
            if grid[r][c] in tank:
                #움직임 돌기
                for move in moves:
                    if move == 'U':
                        #탱크의 방향을 위로 바꿔주고
                        grid[r][c] = '^'
                        #탱크가 맵의 범위 안에 있고, 이동하려는 칸이 평지('.')인 경우에만 이동
                        if 0 <= r-1 < H and grid[r-1][c] == '.':
                            grid[r][c] = '.' #현재 위치 평지로 바꿔주고
                            r -= 1 #탱크의 위치 업데이트
                            grid[r][c] = '^' #새 위치에 탱크 방향 표시
                    #
                    elif move == 'D':
                        #탱크의 방향을 아래로 바꿔주고
                        grid[r][c] = 'v'
                        #탱크가 맵의 범위 안에 있고, 이동하려는 칸이 평지('.')인 경우에만 이동
                        if 0 <= r+1 < H and grid[r+1][c] == '.':
                            grid[r][c] = '.' #현재 위치 평지로 바꿔주고
                            r += 1 #탱크의 위치 업데이트
                            grid[r][c] = 'v' #새 위치에 탱크 방향 표시
                    elif move == 'L':
                        #탱크의 방향을 왼쪽으로 바꿔주고
                        grid[r][c] = '<'
                        #탱크가 맵의 범위 안에 있고, 이동하려는 칸이 평지('.')인 경우에만 이동
                        if 0 <= c-1 < W and grid[r][c-1] == '.':
                            grid[r][c] = '.'
                            #탱크의 위치 업데이트
                            c -= 1
                            #새 위치에 탱크 방향 표시
                            grid[r][c] = '<'
                            
                    elif move == 'R':
                        #탱크의 방향을 오른쪽으로 바꿔주고
                        grid[r][c] = '>'
                        #탱크가 맵의 범위 안에 있고, 이동하려는 칸이 평지('.')인 경우에만 이동
                        if 0 <= c+1 < W and grid[r][c+1] == '.':
                            grid[r][c] = '.'
                            #탱크의 위치 업데이트
                            c += 1
                            grid[r][c] = '>'
                            #탱크가 현재 바라보는 방향으로 포탄 발사
                    elif move == 'S':
                        #탱크의 현재 방향에 따라 포탄이 이동할 방향 결정
                        if grid[r][c] == '^':
                            dr, dc = -1, 0
                        elif grid[r][c] == 'v':
                            dr, dc = 1, 0
                        elif grid[r][c] == '<':
                            dr, dc = 0, -1
                        elif grid[r][c] == '>':
                            dr, dc = 0, 1
                        
                        #포탄이 맵의 범위 안에 있고, 이동하려는 칸이 평지('.')인 경우에만 이동
                        nr, nc = r + dr, c + dc
                        while 0 <= nr < H and 0 <= nc < W:
                            if grid[nr][nc] == '#': #강철벽 만나면 포탄 멈춤
                                break
                            elif grid[nr][nc] == '*': #벽돌벽 만나면 벽돌벽 파괴하고 포탄 멈춤
                                grid[nr][nc] = '.'
                                break
                            nr += dr
                            nc += dc
    #최종 맵 상태 출력
    print(f'#{tc}', end=' ')
                        
    
    