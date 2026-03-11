# 스위치개수
N= int(input())
# 스위치 상태: 0번 인덱스를 버리기 위해 맨 앞에 [-1]을 이어 붙인다
arr = [-1] + list(map(int, input().split()))
# 학생수
S=int(input())
#학생수만큼 반복, 성별과 번호 받기
for _ in range(S):
    sex, num = map(int, input().split())
    
    if sex == 1:
        #스위치 번호가 자기가 받은 수의 배수 = 스위치 상태 변경
        for i in range(1, len(arr)):
            if i % num == 0:
                arr[i] = 1-arr[i] # 0은 1로 1은 0으로 뒤집기
                
    
        # #좌우 대칭이고 가장많은 스위치 포함하는 구역 상태변경
        # for i in range(len(arr)):
        #     if arr[i] == arr[i-1] and arr[i] == arr[i+1]:
        #         arr[i] == arr[i-1] == arr[i+1] = ?
        #     else:
        #         arr[i] == ?
        
        #여학생 정답코드
    else:
        #자기가 밟은 칸 무조건 뒤집기
        arr[num] = 1- arr[num]
        
        #양옆으로 벌릴 팔의 길이(대칭)
        k = 1
        
        #범위 안 벗어나고 양쪽이 대칭일 때만 계속 반복
        while num - k> 0 and num +k <= N and arr[num -k] == arr[num+k]:
            arr[num -k] = 1- arr[num -k]
            arr[num +k] = 1- arr[num +k]
            k+=1
            
# 1번 스위치부터 N번 스위치까지 순서대로 쳐다본다
for i in range(1, N + 1):
    # 스위치 상태를 출력하고, 줄바꿈 대신 띄어쓰기(end=" ")를 한다
    print(arr[i], end=" ")
    
    #  방금 출력한 스위치가 20번째, 40번째, 60번째... 라면?
    if i % 20 == 0:
        print()  # 아무것도 없는 print()를 써서 강제로 줄을 바꾼다!