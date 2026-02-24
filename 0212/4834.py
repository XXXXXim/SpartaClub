T= int(input())
for tc in range(1,T+1):
    N=int(input())
    card = input()
    counts = [0] *10
    for ch in card:
        counts[int(ch)] +=1
        max_count = 0
        max_num = 0
        for i in range(9,-1,-1):
            if counts[i] > max_count:
                max_count = counts[i]
                max_num = i
    print(f'#{tc} {max_count} {max_num})