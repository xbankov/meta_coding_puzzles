from typing import List


# A family of frogs in a pond are traveling towards dry land to hibernate. They hope to do so by hopping across a trail of NN lily pads, numbered from 11 to NN in order.
# There are FF frogs, numbered from 11 to FF. Frog ii is currently perched atop lily pad PiPi​. No two frogs are currently on the same lily pad. Lily pad NN is right next to the shore, and none of the frogs are initially on lily pad NN.
# Each second, one frog may hop along the trail towards lily pad NN. When a frog hops, it moves to the nearest lily pad after its current lily pad which is not currently occupied by another frog (hopping over any other frogs on intermediate lily pads along the way). If this causes it to reach lily pad NN, it will immediately exit onto the shore. Multiple frogs may not simultaneously hop during the same second.
# Assuming the frogs work together optimally when deciding which frog should hop during each second, determine the minimum number of seconds required for all FF of them to reach the shore.
# Constraints
# 2≤N≤10122≤N≤1012
# 1≤F≤500,0001≤F≤500,000
# 1≤Pi≤N−11≤Pi​≤N−1
# Sample test case #1
#
# N = 3
# F = 1
# P = [1]
#
# Expected Return Value = 2
#
# Sample test case #2
#
# N = 6
# F = 3
# P = [5, 2, 4]
#
# Expected Return Value = 4
#
# Sample Explanation
# In the first case, there are 33 lily pads and 11 frog. The frog is initially atop lily pad 11 and will take 22 hops to reach lily pad 33.
# In the second case, there are 66 lily pads, with frogs on lily pads 55, 22, and 44. Initially the lily pads and frog numbers can be represented as .2.31.
# One optimal sequence of hops is:
#
#     Frog 22 hops forward to lily pad 33:
#     ..231.
#     Frog 22 hops over frogs 11 and 33, onto lily pad 66 and exiting onto the shore:
#     ...31.
#     Frog 33 hops over frog 11, onto lily pad 66 and exiting onto the shore:
#     ....1.
#     Frog 11 hops onto lily pad 66, exiting onto the shore.
def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
    return N - min(P)
