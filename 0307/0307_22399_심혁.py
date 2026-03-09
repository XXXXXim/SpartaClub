T = int(input())
for tc in range(1, T + 1):
    # 수정 1: input() 괄호 추가!
    N = int(input())
    arr = list(map(int, input().split()))
    
    # 오름차순 정렬 (소, 중, 대 구분 위한 필수 작업)
    arr.sort()
    
    # 문제 당근 개수가 1000이 최대
    min_diff = 1001
    
    # 칼질 2번으로 3구역 나누기
    # 첫 번째 칼질 (소형 상자 마지막 당근 인덱스)
    for i in range(N - 2):
        # 두 번째 칼질 (중형 상자의 마지막 당근 인덱스)
        for j in range(i + 1, N - 1):
            # 조건 1: 같은 크기 당근 나누면 안 됨
            # 상자 경계선에 있는 당근들이 크기가 다를 때만 포장
            if arr[i] != arr[i+1] and arr[j] != arr[j+1]:
                # 개수 구하기
                s = i + 1
                m = j - i
                l = N - 1 - j
            
                
                cnt = [s, m, l]
                diff = max(cnt) - min(cnt)
                
                # 기존 최소 차이보다 지금 구한 차이가 더 작으면 신기록 갱신
                if min_diff > diff:
                    min_diff = diff
                    
    if min_diff == 1001:
        min_diff = -1
        
    # 수정 2: 출력 형식에 # 추가!
    print(f'#{tc} {min_diff}')