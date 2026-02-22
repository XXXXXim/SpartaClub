T = int(input())
for tc in range(1,T+1):
    A, B, C = map(int, input().split())
    count = 0
    #A<B<C always
    #B를 C보다 작게 만들기
    if B >= C:
        #뉴B는 C보다 딱 1만 작으면됨 (더하면 손해)
        newB = C -1
        #사탕 먹은 개수는 원래 B - newB
        count +- B-newB
        #B 값 수정
        B = newB
    #A를 B보다 작게 만들기    
    if A >= B:
        # 뉴A는 B보다 딱 -1
        newA = B - 1
        # 사탕 먹은 개수는 원래 A -newA
        count+= A-newA
        # A 값 새 설정
        A = newA
    #만약 A나 B가 1보다 작거나 A<B<C아니면 -1 출력
    if A < 1 or B <1 or not (A<B<C):
        count = -1
        
    print(f'#{tc} {count}')
