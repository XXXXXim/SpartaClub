T = int(input())

for tc in range(1, T+1):
    N = int(input())
    #나눌 소수 리스트
    primes = [2, 3, 5, 7, 11]
    #그 소수들을 셀 배열생성
    counts = [0] * 5
   
    #range는 5-1까지 순회
    for i in range(5):
        
        #N을 primes[i]로 나눴을 때
        # 나머지가 0이면 (즉 나눠지면)
        # 계속 반복
        while N % primes[i] == 0:
            #i번째 소수에 카운트+1
            counts[i] += 1
            
            N = N // primes[i]
    
    print(f"#{tc}", *counts)
