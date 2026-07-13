class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            res.append([1] * (i+1))

        if len(res) == 1 or len(res) == 2:
            return res

        for i in range(2,numRows):
            for j in range(1,i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]

        return res

        
