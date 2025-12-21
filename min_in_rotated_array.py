#array of length n, sorted
# rotated between 1 and n times 
# n "shifts" over


#elements are unique
# return the minimum element
# O(logn)


#brute force: treat it as sorted, look through each item O(n)
#sort, and return arr[0] O(nlogn)

# modified binary search
#
# 
# intuition: if you check the middle element, and then you check
# the elements right next to it
# if both are bigger, then its the minimum
# if left is smaller, then the min is in the left half
# if left is bigger, then the min is in the right half
#
# if length is 1, return nums[0]
# if length is 2, return the smaller of the two
#
# O(logn) because its just a modified binary search

class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums)-1

        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid +1
            else:
                r = mid

        return nums[l]


        
