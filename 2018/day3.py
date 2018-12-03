import os
"""
Day 3
of adventofcode
"""
class Counter(dict):
    def __missing__(self, key):
        return 0
# Counter Dictionary structure

Fabric = Counter()
RawInput = open("/home/rcw/projects/python/adventofcode/2018/day3/input", 'r')
for line in RawInput:
    claim = line.split()
    claimLoc = claim[2].split(',')
    claimLoc[1] = int(claimLoc[1][:-1])
    claimLoc[0] = int(claimLoc[0])
    claimSize = claim[3].split('x')
    claimSize[0] = int(claimSize[0])
    claimSize[1] = int(claimSize[1])
    orgLoc = claimLoc
    for ii in range(claimSize[0]):
        claimLoc[1] = orgLoc[1]
        for jj in range(claimSize[1]):
            Fabric[tuple(claimLoc)] += 1
            claimLoc[1] += 1
        claimLoc[0] += 1

print(claimLoc, claimSize)
overlap = 0
for square in Fabric:
    if Fabric[square] > 1:
        overlap += 1
print(overlap)

