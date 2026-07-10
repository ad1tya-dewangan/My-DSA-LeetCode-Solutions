class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    #mark entire row
                    for c in range(cols):
                        if matrix[i][c] != 0:
                            matrix[i][c] = '$'
                    #mark entire col
                    for r in range(rows):
                        if matrix[r][j] != 0:
                            matrix[r][j] = '$'

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '$':
                    matrix[i][j] = 0

        