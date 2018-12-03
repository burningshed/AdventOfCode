import os
"""
Day 3
of adventofcode
"""
class Counter(dict):
    def __missing__(self, key):
        return 0
class Lister(dict):
    def __missing__(self, key):
        return []
# Counter Dictionary structure

Fabric = Counter()
Claims = Lister()
posAns = set()
RawInput = open("/home/rcw/projects/python/adventofcode/2018/day3/input", 'r')
for line in RawInput:
    claim = line.split()
    posAns.add(claim[0])
    claimLoc = claim[2].split(',')
    claimLoc[1] = int(claimLoc[1][:-1])
    claimLoc[0] = int(claimLoc[0])
    claimSize = claim[3].split('x')
    claimSize[0] = int(claimSize[0])
    claimSize[1] = int(claimSize[1])
    orgLoc = claimLoc[:]
    for ii in range(claimSize[0]):
        claimLoc[1] = orgLoc[1]
        for jj in range(claimSize[1]):
            Fabric[tuple(claimLoc)] += 1
            CurSpot = Claims[tuple(claimLoc)]
            CurSpot.append(claim[0])
            Claims[tuple(claimLoc)] = CurSpot
            claimLoc[1] += 1
        claimLoc[0] += 1
overlap = 0
for square in Fabric:
    if Fabric[square] > 1:
        overlap += 1
        for elf in Claims[square]:
            if elf in posAns:
                posAns.remove(elf)
print(overlap)
print(posAns)


