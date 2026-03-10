# 스위치개수
N= int(input())
# 스위치 상태: 0번 인덱스를 버리기 위해 맨 앞에 [-1]을 이어 붙인다
arr = list(map(int, input().split()))
# 학생수
S=int(input())
#학생수만큼 반복, 성별과 번호 받기
for _ in range(S):
    sex, num = map(int, input().split())
    print(arr)
    # if sex == 1:
    #     #스위치 번호가 자기가 받은 수의 배수 = 스위치 상태 변경
    
    # else:
    #     pass