#테스트케이스 수
T = int(input()) 
#1부터 T까지 tc
for tc in range(1, T+1): 
#정수들이 하나씩 나오는 반복가능한 객체
    num = map(int, input().split())
    count = 0 #누적합변수
    #num안에 들어있는 숫자 순회
    for i in num: 
        #i가 홀수인지 검사
        if i%2 == 1:
            #홀수만 누적해서 더함
            count += i
            #결과출력
    print(f'#{tc} {count}')
            
