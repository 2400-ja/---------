#箱出力
def H(S, x, y):
    if(x < len(S) and y < len(S[x])):
        return S[x][y][0]
    
def I(S, x, y):
    if(x < len(S) and y < len(S[x])):
        return S[x][y][1]

#悪い部分の要素
def Bxy(S,x,y,X,u,n):
    if x == X and y == u:
        return (H(S,x,y)-1,I(S,x,y)-1)
    if x == X and y == u+1:
        return (n,n)
    if x != X and y == u+1:
        return (H(S,x,y),n)
    return (H(S,x,y),I(x,y)) 

def expand(S, n):
    #特別ルール : [n] = n
    if S == []:
        return n

    X = len(S)-1

    #一般ルール
    #非零最下箱の高さ    
    u = max([y if H(S,X,y) != 0 else 0 for y in range(len(S[X]))])

    if u == 0:
        return (S[0:-1], n+1)

    #仕切り
    r = max([x if I(S,x,u) < I(S,X,u) else 0 for x in range(X)])

    #悪い部分
    B = [[Bxy(S,x,y,X,u,n) for y in range(len(S[x]))] for x in range(r+1,X+1)]

    #良い部分
    G = [S[x] for x in range(r+1)]

    return (G+B*(n+1),n)

print(expand([[(1,1),(2,2)],[(0,0)]], 3))