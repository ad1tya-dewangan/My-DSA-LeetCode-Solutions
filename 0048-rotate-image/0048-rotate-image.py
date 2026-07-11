class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) # since its a nxn matrix rows==cols

        # Transpose
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        # Reverse each row
        for r in range(n):
            matrix[r] = matrix[r][::-1]