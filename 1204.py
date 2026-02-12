#tc수입력
T=int(input())
#tc 수만큼 반복
for tc in range(1, T+1):
    #tc 번호입력
    case = int(input())
    #점수 입력
    score = list(map(int, input().split()))
    #점수 0~100점 이므로 101개 만큼 리스트 생성
    count = [0] * 101
    #각 점수 몇번나오나 세기
    for s in score:
        #점수 인덱스 사용하여 등장횟수 증가
        count[s] +=1
    #가장 많이 나온 횟수 저장할 변수
    maxs = 0
    #최빈값(정답) 저장할 변수
    answer = 0

    # 0부터 100 점까지 차례로 확인
    for i in range(101):
        #지금 확인한 점수가 가장 많이 나온 횟수보다 크거나 같으면
        if count[i] >= maxs:

            #최대 등장횟수 갱신
            count[i] = maxs
            # 정답은 i 로
            answer = i

    print(f"#{tc} {answer}")


