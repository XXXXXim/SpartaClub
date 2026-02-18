T=int(input())
for tc in range(1,T+1):
    N= int(input())
    card = input()
    
    #0~9 숫자 등장 횟수를 저장할 카운팅 배열
    counts = [0] * 10
    
    #각 숫자의 등장 횟수 세기
    for ch in card:
        counts[int(ch)] +=1
        
        #최대 등장 횟수와 해당 숫자 저장 변수
        max_count = 0
        max_num = 0
        
        #9부터 0까지 거꾸로 탐색
        #(개수가 같을 경우 더 큰 숫자를 선택하기 위함)
        for i in range(9,-1,-1):
            if counts[i]>max_count:
                max_count = counts[i]
                max_num = i
    print(f'#{tc} {max_num} {max_count}')
    
    
