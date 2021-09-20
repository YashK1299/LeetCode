"""
912. Sort an Array
Given an array of integers nums, sort the array in ascending order.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
 

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
"""


import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # self.quicksort(nums, 0, len(nums)-1)
        # return nums
        res = self.mergesort(nums)
        return res
    
    def quicksort(self, arr, low, high):
        if low < high:
            pivot = self.partition(arr, low, high)
            self.quicksort(arr, low, pivot-1)
            self.quicksort(arr, pivot+1, high)
    
    def partition(self, arr, low, high):
        pivot = random.randint(low, high)
        arr[high], arr[pivot] = arr[pivot], arr[high]
        pivot = high
        i = low - 1
        for j in range(low, high):
            if arr[j] < arr[pivot]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[pivot] = arr[pivot], arr[i+1]
        return i+1
    
    def mergesort(self, arr):
        if len(arr)>1:
            mid = len(arr)//2
            left = self.mergesort(arr[:mid])
            right = self.mergesort(arr[mid:])
            arr = self.merge(left, right)
        return arr
    
    def merge(self, left, right):
        i, j = 0, 0
        res = []
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res += left[i:] + right[j:]
        return res