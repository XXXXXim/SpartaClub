T = int(input())  # 전체 테스트 케이스 개수 입력 
for tc in range(1, T+1):
    N = int(input())  # 배열의 길이 
    arr = list(map(int, input().split()))  # 리스트로 입력받기
    
    count = 0  
    #  [1단계: 해체 과정]
    def mergesort(li):
        global count  # 함수 밖에 있는 count 변수를 안에서 수정선언
        
        # 1. 종료 조건: 방에 1명 남았으면 더 쪼갤 수 없으니 그대로 돌려보냄 (리턴)
        if len(li) == 1:
            return li
        
        # 2. 배열의 정중앙 인덱스를 구한다
        mid = len(li) // 2
        right = li[mid:]  # 중간부터 끝까지 (오른쪽 절반)
        left = li[:mid]   # 처음부터 중간 전까지 (왼쪽 절반)
        
        # 3. 쪼갠 걸 다시 mergesort에 넣어서 완벽히 정렬된 결과물을 받아옴
        left_lst = mergesort(left)   
        right_lst = mergesort(right) 
        
        # 핵심로직: 합치기 직전에 왼쪽 끝 방과 오른쪽 끝 방을 검사
        if left_lst[-1] > right_lst[-1]:
            count += 1  # 왼쪽이 더 크면 카운트 1 증가
            
        # 4. 정렬된 두 리스트를 하나로 합침
        mergelst = merge(left_lst, right_lst)
        return mergelst  # 합쳐진 최종 완성품을 위로 보냄!

    #  [2단계: 병합 과정]
    def merge(left, right):
        # 1. 경기장 건설: 왼쪽 팀과 오른쪽 팀 인원수를 합친 크기의 텅 빈 방(result) 만들기
        result = [0] * (len(left) + len(right))
        l = r = 0  # l: 왼쪽 팀 조교, r: 오른쪽 팀 조교 (대기 위치)
        
        # 2. 메인 매치: 두 팀 모두 선수가 남아있을 때만 대결 진행
        while l < len(left) and r < len(right):
            if left[l] < right[r]:  # 오른쪽 선수가 더 크면?
                result[l+r] = left[l]  # 왼쪽 선수가 승리하여 경기장 입장! (l+r 마법의 인덱스)
                l += 1  # 왼쪽 조교는 다음 선수 잡으러 이동
                
            else:  # 왼쪽 선수가 더 크거나 같으면?
                result[l+r] = right[r] # 오른쪽 선수가 승리하여 경기장 입장!
                r += 1  # 오른쪽 조교 이동
                
        # 3. 패잔병 쓸어 담기: 메인 매치 종료 후 남은 팀의 선수들을 싹 다 경기장에 밀어 넣음
        # 왼쪽 팀이 남았을 경우 실행됨 (오른쪽이 남았다면 이 조건문은 False라서 무시됨)
        while l < len(left):
            result[l+r] = left[l]
            l += 1
            
        # 오른쪽 팀이 남았을 경우 실행됨
        while r < len(right):
            result[l+r] = right[r]
            r += 1
            
        # 4. 정렬이 완벽하게 끝난 하나의 리스트를 반환
        return result
    
   
    # ==========================================
    
    # 1. 맨 처음 입력받은 원본 배열(arr)을 mergesort에 던져서 정렬 시작!
    arr_list = mergesort(arr)
                    
    # 2. SWEA 요구사항에 맞춰 정답 출력 
    # 양식: #테스트케이스번호 중앙값(N//2 인덱스) 교차횟수(count)
    print(f'#{tc} {arr_list[N//2]} {count}')