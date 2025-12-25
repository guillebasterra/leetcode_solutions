#inefficient brute force: 
class Solution:
    def climbStairs(self, n: int) -> int:
        #n steps to reach the top
        # every point, do I take one forward, or two?
        if n < 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs(n-1)+ self.climbStairs(n-2)

#runtime: O(2^n), space O(n)


#memoized

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def helper(n):
            if n in memo: return memo[n]
            if n == 1: return 1
            if n == 2: return 2
            memo[n] = helper(n-1)+helper(n-2)
            return memo[n]

        return memo[n]


# optimal, iteration
#
    class Solution:
        def climbStairs(self,n:int)->int:
            one = 1
            two = 0
            for i in range(n):
                temp = one
                one = one + two
                two = temp
            return one




















        
