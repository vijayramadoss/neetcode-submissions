class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=len(matrix)
        col=len(matrix[0])
        roww=[False for i in range(row)]
        coll=[False for i in range(col)]
        change=False
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    roww[i]=True
                    coll[j]=True
                    change=True
        if change:
            for i in range(row):
                for j in range(col):
                    if roww[i] or coll[j]:
                        matrix[i][j]=0
        