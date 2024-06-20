def solveNQueens(n):
        res=[]
        col=[]
        posdiag=[]
        negdiag=[]
        board=[["."]*n for i in range(n)]
        def queen(r):
            if r==n:
                l=["".join(i) for i in board]
                res.append(l)
                return 
            for c in range(n):
                if c in col or (r+c) in posdiag or (r-c) in negdiag:
                    continue
                board[r][c]="Q"
                col.append(c)
                posdiag.append(r+c)
                negdiag.append(r-c)
                queen(r+1)
                board[r][c]="."
                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
        queen(0)
        return res
n=7
print(solveNQueens(n))