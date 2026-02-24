#테스트케이스 수
T = int(input())
#1부터 T까지
for tc in range(1, T+1):
    #정수들이 하나씩 나오는 반복가능한 객체
    num = map(int, input().split())
    #누적합변수
    total = 0
    #num에서 i 순회
    for i in num:
        #i 끝까지 더하기
        total += i
        #누적합 10으로 나누고 round로 반올림
        bmw = round(total/10)

    print(f'#{tc} {bmw}')
