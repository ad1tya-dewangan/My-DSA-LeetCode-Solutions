# Better approach: marking rows and cols for 0 using additional space like sets or arrays 
# TC : O(mn) SC : O(m+n)
# Optimal approach: marking the first row and col inside the matrix 
# TC : O(mn) SC : O(1)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        colZero = False  # for the [0][0] index to identify col marking
        # first pass
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0   # marking first column
                    if j != 0:
                        matrix[0][j] = 0  # marking first row except [0][0]
                    else:
                        colZero = True    # additional marking for the [0][0] index for rows

        # second pass but leaving first row and column (start: 1,1)
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # if [0][0] marking is for rows make entire row 0
        if matrix[0][0] == 0:
            for j in range(cols):
                matrix[0][j] = 0

        # if [0][0] marking is for cols(identified by additional marking) make entire col 0 
        if colZero == True:
            for i in range(rows):
                matrix[i][0] = 0

    


        