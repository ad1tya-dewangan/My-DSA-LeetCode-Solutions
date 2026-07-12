# Intuition:
# Use four boundaries (left, right, top, bottom) to represent the
# current unvisited rectangle.
#
# Traverse the rectangle clockwise:
# top row -> right column -> bottom row -> left column.
#
# After traversing each side, shrink its boundary inward.
#
# The bottom and left traversals require extra boundary checks because
# the top and right traversals may have already exhausted the remaining
# rectangle. Without these checks, elements in a single row/column could
# be visited twice.

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