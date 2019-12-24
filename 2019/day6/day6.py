"""
Advent of Code Day 6
Counting Direct and Indirect orbits
"""

FILE_PATH = "day6.in"

# This creates an object that contains all the data in the file you saved
RawInput = open(FILE_PATH, 'r')

class Satellite:
    def __init__(self, prime, name):
        self.name = name
        self.prime = prime
        self.sats = []

    def has_direct_sat(self, tar):
        if self.name == tar:
            return True
        for sat in self.sats:
            if sat.name == tar:
                return True
        return False

    def has_indirect_sat(self, tar):
        if self.name == tar:
            return True
        for sat in self.sats:
            if sat.has_indirect_sat(tar) == True:
                return True
        return False

    def add_sat(self, tar):
        for sat in self.sats:
            if sat.name == tar:
                return 0
        self.sats.append(Satellite(self, tar))
        return 1

    def addSat_chain(self, prime, sat):
        if self.name == prime:
            self.add_sat(sat)
            return True
        if not self.has_indirect_sat(prime):
            return False
        found = False
        for s in self.sats:
            found = found or s.addSat_chain(prime, sat)

    def get_orbits(self):
        tot_orbs = 0
        for sat in self.sats:
            tot_orbs += 1
            tot_orbs += sat.get_orbits()
        return tot_orbs

    def get_di_orbits(self, prime_orbs):
        tot = 0
        for sat in self.sats:
            tot += sat.get_di_orbits(prime_orbs+1)
        return prime_orbs+tot

    def find_com_star(self, a, b):
        """
        find last common star for a, b
        """
        if (self.has_indirect_sat(a) and
            self.has_indirect_sat(b)):
            target = None
            for sat in self.sats:
                target = sat.find_com_star(a, b)
                if target is not None:
                    return target
            if target == None:
                return self
        return None

    def find_dist(self, a):
        """
        find distance to a
        """
        tot = 0
        if self.name == a:
            return 0
        if not self.has_indirect_sat(a):
            return 0
        for sat in self.sats:
            tot += sat.find_dist(a)
        return tot + 1

class Star_Map:
    def get_tot_orbits(self):
        return self.head.get_di_orbits(0)
    def __init__(self, COM):
        """
        unsure how to init this
        """
        self.head_name = COM

    def buildMap(self, raw_star_map):
        self.head = Satellite(None, self.head_name)
        
        star_dict = self.raw_star_map_to_dict(raw_star_map)
        self.buildMap_helper(star_dict, self.head_name)

    def buildMap_helper(self, star_dict, cur_star):
        try:
            for star in star_dict[cur_star]:
                self.head.addSat_chain(cur_star, star)
                self.buildMap_helper(star_dict, star)
        except KeyError:
            return 0

    def raw_star_map_to_dict(self, raw):
        """
        dict should be in form key: [list of stars]
        """
        star_dict = {}
        for pair in raw:
            key = pair[0]
            try:
                star_dict[key].append(pair[1])
            except KeyError:
                star_dict[key] = [pair[1]]
        return star_dict

    def get_path_dist(self, a, b):
        """
        find distance of shortest path between a and b
        """
        temp_head = self.head.find_com_star(a, b)
        tot = temp_head.find_dist(a) + temp_head.find_dist(b)
        return tot



Test_Input = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L"
Part2_test = "\nK)YOU\nI)SAN"

Test_Input += Part2_test
# for each line in the file
sats = []
for line in RawInput:
    line = line.rstrip()
    orbitee, orbitor = line.split(')')
    sats.append((orbitee,orbitor))
test_sats = []
for line in Test_Input.split('\n'):
    orbitee, orbitor = line.split(')')
    test_sats.append((orbitee,orbitor))

sm = Star_Map("COM")
sm.buildMap(sats)
#print(sm.get_tot_orbits())
ans = sm.get_path_dist('YOU', 'SAN')
print(ans)
# Answer will be 2 higher then it should be
