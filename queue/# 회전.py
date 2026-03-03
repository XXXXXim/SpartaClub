# 회전
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    q = [0] * (N * M + 100)
    front = rear = -1
    
    #arr의 원소를 맨 앞부터 차례로 q에 삽입
    for item in arr:
        rear += 1
        q[rear] = item
    #q의 맨 앞에서 원소를 꺼내서 꺼넨 원소를 다시 맨 뒤로 삽입하는 연산을 M번 반복
    for i in range(M):
        front += 1
        item = q[front]
        rear += 1
        q[rear] = item