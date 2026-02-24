T=int(input())
for tc in range(1, T+1):
    N = int(input())
    #본 숫자들 집합(중복제거)
    seen = set()
    #몇번센건지 확인하는 k
    k = 0
    # 0~9 나올때까지 다 반복하기
    while len(seen) < 10:
        k +=1               #몇번째인지 증가함
        num = N*k           #kN - 배수계산
        
        for i in str(num):  #숫자를 문자열로 바꿔서 반복
            seen.add(i)     #집합에 추가한다

    print(f'#{tc} {num}')