from itertools import product


# Note: Chapter 2 is a harder version of this puzzle. The only difference is a larger constraint on NN. A photography
# set consists of NN cells in a row, numbered from 11 to NN in order, and can be represented by a string CC of length
# NN. Each cell ii is one of the following types (indicated by CiCi​, the iith character of CC):
#
#     If CiCi​ = “P”, it is allowed to contain a photographer
#     If CiCi​ = “A”, it is allowed to contain an actor
#     If CiCi​ = “B”, it is allowed to contain a backdrop
#     If CiCi​ = “.”, it must be left empty
#
# A photograph consists of a photographer, an actor, and a backdrop, such that each of them is placed in a valid
# cell, and such that the actor is between the photographer and the backdrop. Such a photograph is considered
# artistic if the distance between the photographer and the actor is between XX and YY cells (inclusive),
# and the distance between the actor and the backdrop is also between XX and YY cells (inclusive). The distance
# between cells ii and jj is ∣i−j∣∣i−j∣ (the absolute value of the difference between their indices). Determine the
# number of different artistic photographs which could potentially be taken at the set. Two photographs are
# considered different if they involve a different photographer cell, actor cell, and/or backdrop cell. Constraints
# 1≤N≤2001≤N≤200 1≤X≤Y≤N1≤X≤Y≤N Sample test case #1
#
# N = 5
# C = APABA
# X = 1
# Y = 2
#
# Expected Return Value = 1
#
# Sample test case #2
#
# N = 5
# C = APABA
# X = 2
# Y = 3
#
# Expected Return Value = 0
#
# Sample test case #3
#
# N = 8
# C = .PBAAP.B
# X = 1
# Y = 3
#
# Expected Return Value = 3
#
# Sample Explanation In the first case, the absolute distances between photographer/actor and actor/backdrop must be
# between 11 and 22. The only possible photograph that can be taken is with the 33 middle cells, and it happens to be
# artistic. In the second case, the only possible photograph is again taken with the 33 middle cells. However,
# as the distance requirement is between 22 and 33, it is not possible to take an artistic photograph. In the third
# case, there are 44 possible photographs, illustrated as follows: .P.A...B .P..A..B ..BA.P.. ..B.AP.. All are
# artistic except the first, where the artist and backdrop exceed the maximum distance of 33.
def find_photographs(C):
    Ps = []
    As = []
    Bs = []
    for i in range(len(C)):
        if C[i] == "P":
            Ps.append(i)
        elif C[i] == "A":
            As.append(i)
        elif C[i] == "B":
            Bs.append(i)
    return Ps, As, Bs


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    # Write your code here
    artistic = 0
    Ps, As, Bs = find_photographs(C)
    for a in As:
        for p, b in list(product(Ps, Bs)):
            if X <= abs(a - p) <= Y and X <= abs(a - b) <= Y and (p < a < b or b < a < p):
                artistic += 1
    return artistic
