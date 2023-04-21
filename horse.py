# N = int(input())
# xBeg, yBeg = map(int, input().split())
# xEnd, yEnd = map(int, input().split())
N=5
xBeg, yBeg=0, 0
xEnd, yEnd=4, 4
board=[[None] * N for _ in range(N)]
q=[[[xBeg, yBeg]]]
step=0
board[xBeg][yBeg]=step
flag=True
while flag:
    tmp = []
    for i in range(len(q)):
        x, y = q[i][-1][0], q[i][-1][1]
        if x+2<N and y+1<N and board[x+2][y+1]==None:
            board[x+2][y+1]=step+1
            tmp.extend([q[i].copy()])
            tmp[-1].extend([[x+2,y+1]])
            if x+2==xEnd and y+1==yEnd:
                flag=False
                res=tmp[-1]
        if x+1<N and y+2<N and board[x+1][y+2]==None:
            board[x+1][y+2]=step+1
            tmp.extend([q[i].copy()])
            tmp[-1].extend([[x+1,y+2]])
            if x+1==xEnd and y+2==yEnd:
                flag=False
                res=tmp[-1]
        if x-2>-1 and y-1>-1 and board[x-2][y-1]==None:
            board[x-2][y-1]=step+1
            tmp.extend([q[i].copy()])
            tmp[-1].extend([[x-2,y-1]])
            if x-2==xEnd and y-1==yEnd:
                flag=False
                res=tmp[-1]
        if x-1>-1 and y-2>-1 and board[x-1][y-2]==None:
            board[x-1][y-2]=step+1
            tmp.extend([q[i].copy()])
            tmp[-1].extend([[x-1,y-2]])
            if x-1==xEnd and y-2==yEnd:
                flag=False
                res=tmp[-1]
        if x+2<N and y-1>-1 and board[x+2][y-1]==None:
            board[x+2][y-1]=step+1
            tmp.extend([q[i].copy()])
            tmp[-1].extend([[x+2,y-1]])
            if x+2==xEnd and y-1==yEnd:
                flag=False
                res=tmp[-1]
        if x+1<N and y-2>-1 and board[x+1][y-2]==None:
            board[x+1][y-2]=step+1
            tmp.extend([q[i].copy()])
            tmp[-1].extend([[x+1,y-2]])
            if x+1==xEnd and y-2==yEnd:
                flag=False
                res=tmp[-1]
        if x-2>-1 and y+1<N and board[x-2][y+1]==None:
            board[x-2][y+1]=step+1
            tmp.extend([q[i].copy()])
            tmp[-1].extend([[x-2,y+1]])
            if x-2==xEnd and y+1==yEnd:
                flag=False
                res=tmp[-1]
        if x-1>-1 and y+2<N and board[x-1][y+2]==None:
            board[x-1][y+2]=step+1
            tmp.extend([q[i].copy()])
            tmp[-1].extend([[x-1,y+2]])
            if x-1==xEnd and y+2==yEnd:
                flag=False
                res=tmp[-1]
    q, step=tmp, step+1
print('Steps:', step)
print(res)