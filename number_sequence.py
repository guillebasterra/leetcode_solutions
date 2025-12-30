#single player board game with n positions
# each position can be empty (".")
# T
# or C
# Player may possess many tokens T
# Coin is collected by the player when a token is put on the coin's position
#
# each coin can be collected only once
# the player can move a token by exactly three positions to the right (in one turn)
#
# input: string of board game return: max number of coins the player can collect
#  example input  = "TT.CC" return 2
#
#  each token can only travel on its own "rail", denoted by its index % 3
#  take the string "TTTCCCCTTC."
#  the rails would be:
#  "TCCC"
#  "TCT"
#  "TC"
#  we can just find the leftmost token for each trail and then count the coins in front of it...
#

class Solution:
    def findCoins(self, board: str) -> int:
        max_coins = 0

        for i in {0,1,2}:
            firstT = 0
            for j in range(i,len(board),2):
                if board[j] == 'T':
                    firstT = 1
                if firstT and board[j] == 'C':
                    max_coins +=1
        return max_coins

#runtime: O(n)
# space: O(1)

