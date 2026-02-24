T = int(input())
for tc in range(1,T+1):
    N= int(input())
    
    grid = [[0]*10 for _ in range(10)]
    purple = 0
    
    for _ in range(N):
        r1,c1,r2,c2,color = map(int, input().split())
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                if color == 1:
                    if grid[i][j] == 2:
                        purple+=1
                    grid[i][j] = 1
                if color == 2:
                    if grid[i][j] ==1:
                        purple+=1
                    grid[i][j] = 2
                    
                    
                
    print(f'{tc} {purple}')