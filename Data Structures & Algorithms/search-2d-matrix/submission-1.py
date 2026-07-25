class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        size=(row*col)
        left=0
        right=size-1
        out=False
        while(left<=right):
            mid=left+(right-left)//2
            r=mid//col
            c=mid%col
            if(matrix[r][c]==target):
                out=True
                return out
            elif(matrix[r][c]>target):
                right=mid-1
            else:
                left=mid+1   
        return out