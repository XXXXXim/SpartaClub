T= int(input())
for tc in range(1,T+1):
    #목표 메모리 상태입력
    target = input().strip()
    #수정 횟수 저장 변수
    count = 0
    #현재 메모리 상태
    #초기상태는 항상 전부 0이므로 시작은 '0'
    current = '0'
    for ch in target:
    #목표 문자열을 왼쪽부터 하나씩 확인
        if ch != current:
        #현재 상태와 목표 비트가 다르면
            count+=1
            #한 번 수정해야하므로 카운트 증가
            current = ch
            #현재상태를 목표 비트로 변경(뒤는 전부 자동으로 바뀜)
    print(f'#{tc} {count}')

