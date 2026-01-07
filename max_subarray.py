# given an integer array nums
# find the subarray with the largest sum
# return its sum
#
#
# input is a integer array
# find the subarray with the largest sum
# Return the sum (int)
#
# the array is not sorted?
# Can the numbers be negative?
# how big the numbers are, how long the array is?
# length is at least 1
# [1, 2, 3 ,4 ,-1, 0]
# key insight to this problem is that sometimes its going to be worth it 
# to keep negative numbers, and sometimes its not
#
# if our sum up to this point is overwritten by the next number, then you want to reset
# [-4, 4, -5, 2]
#
# [1,2,3,-6,8]
#
# brute force: track of your current sum, test every subarray, return the largest sum you find
# O(n^2) this is clearly not optimal
#
# check every number, order matters 
# one pass solution
#
#curr_sum


def maxSubarray(self, nums: List[int]) -> int:


    curr_sum = 0
    max_sum = nums[0]

    for num in nums:
        if curr_sum <= 0: curr_sum = 0
        curr_sum += num
        max_sum = max(max_sum, curr_sum)
    return max_sum



[1, 3, -4, 5]

currsum = 1
maxsum = 1

currsum = 4
maxsum = 4

currsum = 0
max_sum = 4

curr_sum = 5
max_sum = 5

retuern 5


[1]
curr_sum = 1

[-5]


