"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        while i < len(matrix):
            if matrix[i][0] > target:
                break
            i+=1
        i -= 1
        return self.search(matrix[i], 0, len(matrix[0])-1, target)
        
    def search(self, arr, low, high, target):
        if low <= high:
            mid = (low+high)//2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                return self.search(arr, low, mid-1, target)
            else:
                return self.search(arr, mid+1, high, target)
        return False
