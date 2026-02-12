T = int(input())
for tc in range(1, T+1):
    #이번 tc에서 색칠할 직사각형 개수
    N = int(input())
    # ******10x10 격자판 만들기******
    board = [[0] * 10 for _ in range(10)]
    #색칠영역을 N번 처리하기
    for _ in range(N):
        #수열 입력받아 각 변수에 저장
        r1, c1, r2, c2, color = map(int, input().split())

        for r in range(r1,r2+1):
            for c in range(c1, c2+1):
                board[r][c] += color
 
    cnt = 0
    for i in range(10):
        for j in range(10):
            if board[i][j]==3:
                cnt+=1
    print(f'#{tc} {cnt}')

