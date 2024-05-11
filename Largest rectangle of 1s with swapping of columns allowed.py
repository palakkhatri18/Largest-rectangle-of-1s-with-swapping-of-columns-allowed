#Given a matrix mat of size R*C with 0 and 1s, find the largest rectangle of all 1s in the matrix. The rectangle can be formed by swapping any pair of columns of given matrix.
class Solution:
    def getMaxArea(self, a):
        a.sort()
        n = len(a)
        ans = 0
        for i in range(n):
            ans = max(ans, a[i] * (n - i))
        return ans

    def maxArea(self, mat, r, c):
        # Initialize auxiliary matrix
        aux = [[0] * c for _ in range(r)]
        
        # Fill auxiliary matrix
        for i in range(r):
            for j in range(c):
                aux[i][j] = 1 if mat[i][j] else 0
                if i > 0:
                    if aux[i][j]:
                        aux[i][j] += aux[i - 1][j]
        
        # Calculate maximum area of rectangle
        ans = 0
        for row in aux:
            ans = max(ans, self.getMaxArea(row))
        
        return ans