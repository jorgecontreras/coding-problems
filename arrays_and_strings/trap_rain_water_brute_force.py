# TRAPPING RAIN WATER 
# 
# Brute Force
# 
# Time complexity: O(N^2)
# Space complexity: O(1) 
#
#        #
#    #   ## #
# _#_##_######
# 001012100100
#
# Intuition:
#
# 1. for each array element, find next equal or larger number to the right and to the left. 
# 2. get the min of the two (if found) and substract height of current element.
# 3. sum all the units
#
#
#      x
# x    x
# x  x x
# xx xxx
# xx_xxx
# 024120

def calculate_water_volume(elevation_map):
    
    volume = 0

    for i, e in enumerate(elevation_map):
        l = r = i
        lh = rh = 0

        # find max higher to the left
        while l > 0: 
            l -= 1
            if lh < elevation_map[l] > e:
                lh = elevation_map[l]

        # find max higher to the right
        while r < len(elevation_map) - 1:
            r += 1
            if rh < elevation_map[r] > e:
                rh = elevation_map[r]

        # will hold at most lowest of the two minus the height of itself
        lowest = min(lh, rh)
        volume += max(lowest - e, 0)
            
    return volume

elevation_map_1 = [0,1,0,2,1,0,1,3,2,1,2,1]
elevation_map_2 = [4,2,0,3,2,5]

assert calculate_water_volume(elevation_map_1) == 6
assert calculate_water_volume(elevation_map_2) == 9

print("all tests passed.")