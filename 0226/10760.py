T = int(input())
for tc in range(1, T + 1):
    # 1. 격자의 크기 N(행)과 M(열) 입력받기
    N, M = map(int, input().split())
    
    # 2. N x M 화성 표면 높이 격자 입력받기
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    # 3. 8방향 델타 배열 설정
    # 순서: 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]
    
    # 착륙 가능한 후보지 개수를 셀 변수
    spot = 0
    
    # 4. 2차원 배열 전체 순회
    for r in range(N):
        for c in range(M):
            # 현재 칸 주변의 '낮은 지역' 개수를 세기 위한 변수
            lower_count = 0 
            
            # 5. 현재 위치에서 8방향으로 고개를 돌려보기
            for d in range(8):
                # step이 필요 없으므로 바로 방향만 더해줍니다.
                nr = r + dr[d]
                nc = c + dc[d]
                
                # 격자 범위를 벗어나지 않는지 확인 (열의 크기는 M이므로 nc < M 입니다!)
                if 0 <= nr < N and 0 <= nc < M:
                    # 6. 주변 지역의 높이가 현재 위치의 높이보다 '낮은' 경우에만 카운트!
                    if grid[nr][nc] < grid[r][c]:
                        lower_count += 1
            
            # 7. 8방향 검사가 다 끝난 후, 낮은 지역이 4곳 이상이라면 후보지 합격!
            if lower_count >= 4:
                spot += 1
                
    # 8. 최종 후보지 개수 출력
    print(f"#{tc} {spot}")