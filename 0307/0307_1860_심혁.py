# T = int(input())
# for tc in range(1,T+1):
#     #N: 붕어빵 예약한 사람 수 N명
#     #M: 붕어빵 만드는데 걸리는 시간 M초
#     #K: 완성된 붕어빵 K개
#     N, M, K = map(int, input().split())
#     # N개의 정수 sec은 각 사람이 언제도착하는지 초단위
#     sec = list(map(int, input().split()))
#     #초기 답은 불가능으로 정한다
#     answer = "Impossible"
#     # 사람들이 언제 도착하는지 리스트를 순회한다
#     for i in sec:
#         # 만약 i번재 사람이 걸리는 시간 i의 범위가
#         if 0<sec[i]<int(N):
#             # i가 0보다 크고 M보다 작으면
#             if 0<i<M:
#                 #가능
#                 answer = "Possible"
#             #i가 K보다 크면
#             elif i > K:
#                 #불가능
#                 answer = "Impossible"
#             #그외
#             else:
#                 #불가능
#                 answer = "Impossible"
        
#     print(f'#{tc} {answer}')
    
    ##오답노트
    # 1. for i in sec:에서 sec[i]를 쓸 경우 sec이 [3,4]라면 i는 인덱스 (0,1)가 아니라
    #    실제값인 3,4가 나오고 다시 sec[3]이런식으로 넣으면 리스트에 [3]이 없으므로 터진다.
    # 2. 무조건 먼저 온 손님부터 처리해야 하므로 sec.sort로 손님들을 시간순정렬했어야 함
    # 3. elif i > K: (도착 시간이 붕어빵 개수보다 크면 불가?)
    #    i는 시간이고 K는 붕어빵 개수인데 비교하면 안됨
    #    - 게다가 0 < i < M일 때 Possible이라고 했는데, M초가 되기 전에는 빵이 0개야. 
    #      손님이 빵 0개일 때 오면 무조건 Impossible이 되어야 해!
    # 4. break 부재
    
    ##정답코드
T = int(input())
for tc in range(1,T+1):
    #N: 붕어빵 예약한 사람 수 N명
    #M: 붕어빵 만드는데 걸리는 시간 M초
    #K: 완성된 붕어빵 K개
    N, M, K = map(int, input().split())
    # 손님들이 도착하는 시간들을 입력받아서 sec에 저장
    sec = list(map(int, input().split()))
    #*마구잡이로 도착한 손님들을 빨리온 순서로 정렬
    sec.sort()
    # 기본정답 가능으로
    answer = "Possible"
    #줄 서 있는 0번 손님부터 N-1 손님까지 한명씩 심사시작
    for i in range(N):
        #심사받는 i번째 손님이 도착한 진짜시간(초) time에 담기
        time = sec[i]
        #지금 이 손님이 도착한 시간(time)까지 진기가 만든붕어빵 누적개수
        #2초마다 3개 만드는데 5초에 왔으면? 5//2=2번 구웠고 2*3=6개 만들어짐
        made_bread = (time//M)*K
        # i는 0부터 시작하니까, 지금까지 내 가게에 들어온 손님 수(나 포함)는 (i + 1)명!
        # 만들어진 빵보다 먹어야 할 사람 수가 더 많으면?!
        if made_bread < (i+1):
            #빵모자람
            answer = "Impossible"
# 1명이라도 못 먹으면 실패니까, 뒤에 남은 손님은 볼 것도 없이 반복문 즉시 탈출! (덮어쓰기 방지)
            break
        

# 핵심로직
# 1. 손님 대기 줄을 입력받고 먼저 온 순서대로 정렬해야 한다.
# 2. 줄을 검사하고 손님이 실제로 온 시간을 time 변수에 저장한다.
# 3. (time//M)*K 계산을 통해 실제 구워진 빵 개수를 확인하고 빵을 줄 수 있는지 확인
# 4. 만약 줄 빵보다 손님 수가 많으면 실패한다는 것을 기록해야 한다.
# 5. 실패할 경우 뒷 손님은 볼 필요도 없이 break