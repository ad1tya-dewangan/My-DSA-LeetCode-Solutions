class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        # initalizing the triangle by filling it with 1s
        for i in range(numRows):
            res.append([1] * (i+1))

        # starting from 3rd row compute only the middle values
        for i in range(2,numRows):
            for j in range(1,i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]

        return res
        

        
