t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    arr=[]
    for i in range(n):
        ele=list(map(int,input().split()))
        arr.append(ele)
    startx,starty=map(int,input().split())
    startx-=1
    starty-=1
    move=[[-1 for j in range(m)] for i in range(n)]
    move[startx][starty]=0
    level=[[startx,starty]]
    while(len(level)!=0):
        x,y=level.pop(0)
        man=arr[x][y]
        for i in range(max(0,x-man),min(n,x+man+1)):
            j1=y-(man-abs(x-i))
            j2=y+(man-abs(x-i))
            if(move[i][j1]==-1 and j1>=0):
                move[i][j1]=move[x][y]+1
                level.append([i,j1])
            if(move[i][j2]==-1 and j2<m):
                move[i][j2]=move[x][y]+1
                level.append([i,j2])
    q=int(input())
    for _ in range(q):
        x,y=map(int,input().split())
        print(move[x-1][y-1])