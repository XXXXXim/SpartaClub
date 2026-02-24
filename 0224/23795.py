# 테스트 케이스 수 입력
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    # N x N 격자 입력 받기
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 1. 델타 설정 (상, 하, 좌, 우)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 2. 괴물 위치 모두 찾기
    monsters = []
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                monsters.append((r, c))

    # 3. 괴물마다 레이저 발사!
    for r, c in monsters: # 모든 괴물에 대해
        for i in range(4): # 4방향으로
            nr, nc = r + dr[i], c + dc[i]

            # 4. 벽을 만나거나 맵 밖으로 나갈 때까지 '직진' (핵심!)
            while 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 1: # 벽(1)을 만나면 레이저 종료
                    break
                
                if arr[nr][nc] == 0: # 빈칸이면 레이저 맞음 처리
                    arr[nr][nc] = 3  # 0을 3으로 바꿔서 '위험함' 표시
                
                # 다음 칸으로 계속 직진
                nr += dr[i]
                nc += dc[i]

    # 5. 안전한 칸(0) 세기
    safe_count = 0
    for row in arr:
        safe_count += row.count(0)

    print(f"#{test_case} {safe_count}")