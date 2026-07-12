# The intuition is to create 4 pointers to keep track of boundries and srink them after traversal of a boundary until there is no rectangle boundries left
# i.e. left bound. <= right bound. and top bound. <= bottom bound.

# Also make sure a boundary exist before traversing it 
# left <= right will check if the left boundary exist or not
# similarly top <= bottom will check for bottom boundary 

# Note: the top and right boundary doesn't need extra check because the loop will not run if there is no boundary but bottom and left need check because the spiraling is running clockwise and we are shrinking the boundaries inside while loop

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = n-1
        top = 0
        bottom = m-1

        ans = [] #resultant list

        while left <= right and top <= bottom:

            #traversing top
            for i in range(left,right+1):
                ans.append(matrix[top][i])

            top += 1

            #traversing right
            for i in range(top,bottom+1):
                ans.append(matrix[i][right])

            right -= 1

            #traversing bottom 
            # check for bottom boundary
            if top <= bottom:  
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])

                bottom -= 1

            #traversing left
            # check for left boundary
            if left <= right:
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])

                left += 1

        return ans