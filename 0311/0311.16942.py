T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))


def patition(A, l, r):
    # 1. 중간 피벗 선택 전략
    # 배열의 중간 인덱스를 구하여 맨 앞의 원소와 자리를 바꾼다.
    # 이미 정렬된 배열이 입력될 경우 발생하는 최악의 시간복잡도를 방지하기 위함이다.
    mid = (l + r) // 2
    A[l], A[mid] = A[mid], A[l]
    
    # 2. 초기화
    # 피벗(p)은 자리바꿈을 통해 맨 앞으로 온 중간값으로 설정한다.
    p = A[l]  
    i = l
    j = r
    
    # 3. 교차 전까지 탐색 및 스왑
    while i <= j:
        # 왼쪽 탐색: 피벗보다 큰 값을 찾을 때까지 i를 증가시킨다.
        while i <= j and A[i] <= p:
            i += 1
            
        # 오른쪽 탐색: 피벗보다 작은 값을 찾을 때까지 j를 감소시킨다.
        while i <= j and A[j] >= p:
            j -= 1
            
        # i와 j가 교차하지 않았다면, 잘못된 위치에 있는 두 원소를 교환한다.
        if i < j:
            A[i], A[j] = A[j], A[i]
            
    # 4. 피벗의 최종 위치 확정
    # 탐색이 완료되어 교차(i > j)되면, 피벗을 j의 위치와 교환한다.
    # j는 피벗보다 작은 그룹의 마지막 인덱스이기 때문이다.
    A[l], A[j] = A[j], A[l]
    return j

def quicksort(A, l, r):
    # 배열의 크기가 2개 이상일 때만 분할 정복을 수행한다.
    if l < r:
        # 파티션을 통해 피벗의 위치(p)를 확정한다.
        p = patition(A, l, r)  
        # 확정된 피벗을 제외하고 왼쪽 구역을 재귀 호출하여 정렬한다.
        quicksort(A, l, p - 1) 
        # 확정된 피벗을 제외하고 오른쪽 구역을 재귀 호출하여 정렬한다.
        quicksort(A, p + 1, r) 


    
    # 배열의 처음(0)부터 끝(N-1)까지 퀵 정렬을 수행한다.
    quicksort(arr, 0, N - 1)
    
    # 문제 요구사항에 맞춰 중앙값을 출력한다.
    print(f'#{tc} {arr[N//2]}')