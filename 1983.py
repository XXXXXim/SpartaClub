T = int(input()) #테스트케이스 입력
# 미리 등급표를 만들어 둔다
# 인덱스 0이 A+, 1이 A0, ... 9가 D0
grades = ["A+", "A0", "A-", "B+", "B0", "B-",
          "C+", "C0", "C-", "D0"]
#테스트케이스 반복
for tc in range(1, T + 1):
    #N = 학생수
    #K = 학점알고싶은 학생
    #반복가능한 객체로 정의
    N, K = map(int, input().split())
    # 모든 학생의 총점을 저장할 리스트 
    scores = []
    # K번 학생의 총점을 따로 저장할 변수
    target_score = 0
    #학생수만큼 순회하기(학생번호는 1번이 시작)
    for i in range(1, N + 1):
        #중간, 기말, 과제점수 
        mid, final, hw = map(int, input().split())
        #총점 total은 각 항목에 가중치를 곱해서 구함
        total = mid * 0.35 + final * 0.45 + hw * 0.20
        #리스트에 총점을 추가합니다
        scores.append(total)
        # 만약 지금학생이 K번 학생이면
        if i == K:
            #그 학생의 총점 기록
            target_score = total
    #점수리스트를 내림차순 정렬합니다(고득점학생이 앞으로)
    scores.sort(reverse=True)
    #K번 학생의 총점이 몇번짼지 찾는다
    idx = scores.index(target_score)
    # 한 등급당 학생 수는 N // 10 명
    # idx를 그 값으로 나누면 등급 위치가 나온다
    grade = grades[idx // (N // 10)]

    print(f"#{tc} {grade}")
