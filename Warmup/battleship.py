# You're playing Battleship on a grid of cells with RR rows and CC columns. There are 00 or more battleships on the
# grid, each occupying a single distinct cell. The cell in the iith row from the top and jjth column from the left
# either contains a battleship (Gi,j=1Gi,j​=1) or doesn't (Gi,j=0Gi,j​=0).
# You're going to fire a single shot at a random cell in the grid. You'll choose this cell uniformly
# at random from the R∗CR∗C possible cells. You're interested in the probability that the cell hit by your shot
# contains a battleship.
# Your task is to implement the function getHitProbability(R, C, G) which returns this probability.
# Note: Your return value must have an absolute or relative error of at most 10−610−6 to be considered correct.
# Constraints
# 1≤R,C≤1001≤R,C≤100
# 0≤Gi,j≤10≤Gi,j​≤1
# Sample test case #1
#
# R = 2
# C = 3
# G = 0 0 1
#     1 0 1
#
# Expected Return Value = 0.50000000
#
# Sample test case #2
#
# R = 2
# C = 2
# G = 1 1
#     1 1
#
# Expected Return Value = 1.00000000
#
# Sample Explanation
# In the first case, 33 of the 66 cells in the grid contain battleships. Therefore,
# the probability that your shot will hit one of them is 3/6=0.53/6=0.5.
# In the second case, all 44 cells contain battleships, resulting in a probability of 1.01.0 of hitting a battleship.

from typing import List


def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
    # Write your code here
    ships = sum([cell for row in G for cell in row])
    total = R * C
    return ships / total
