T=int(input())
for tc in range(1,T+1):
    #솔루션
    # 1. N입력받고 NxN격자 리스트 생성
    # 2. 이중 for문으로 격자 모든칸 완전탐색(순회)
    # 3. 방향별 연속성확인:if 현재칸 'o'있다면 미리 정의해둔 4가지 방향으로
    #    총 4번 더 나아가며 연속으로 돌있는지 확인
    # 4. 범위체크)제한사항) 이동할 좌표가 격자 밖으로 벗어나지 않는지(0<=좌표<N)확인
    N = int(input())
    #NxN 격자 입력받기(문자열 자체를 리스트로)
    grid = [input() for _ in range(N)]
    # 델타탐색을 위한 방향벡터 설정(우, 하, 우하대각선, 좌하대각선)
    #  dr(row)는 행의 이동, dc(col)은 열의 이동
    dr = [0,1,1,1]
    dc = [1,0,1,-1]
    
    #오목이 완성되었는지 확인할 변수
    omok = False
    
    # 2차원 배열 전체 순회
    for r in range(N):
        for c in range(N):
            #돌있을때만 연속성 검사
            if grid[r][c] == 'o':
                
                # 4가지 방향 각각검사
                for d in range(4):
                    count =1 #시작점에 돌 있는거니까 1부터 시작
                    
                    #해당 방향으로 최대 4칸 더 이동하며 확인 (총5개)
                    for step in range(1,5):
                        nr = r+dr[d] * step
                        nc = c+dc[d] * step
                        
                        # 격자범위 안벗어나고 위치값이 'o'인지 확인
                        if 0 <= nr < N and 0 <= nc< N and grid[nr][nc] == 'o':
                            count+=1
                        else:
                            break #조건에 맞지않으면 현재방향 탐색 중단
                        
                    #5개가 연속 있으면 오목 성공
                    if count == 5:
                        omok = True
                        break
    if omok:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')