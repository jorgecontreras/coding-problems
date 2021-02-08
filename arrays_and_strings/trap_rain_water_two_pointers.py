# TRAPPING RAIN WATER
# 
# Two Pointers
#
# Time complexity: O(N)
# Space complexity: O(1)
#
# Intuition: 
# 
# The idea is to "trap" the water between two pointers (left and right)
# The amount of water depends on where the higher points (e1 and e2) are at a given moment.
# e1 and e2 start at zero but are adjusted as we move the pointers closer together.
# We will have water when the elevation is lower than the higher points
#
#        #
#    #   ## #
# _#_##_######

def calculate_water_volume(elevation_map):
    # initialize variables
    volume = 0
    e1 = e2 = 0
    left = 0
    right = len(elevation_map)-1

    # while there are still points to check
    while left < right:
        if elevation_map[left] < elevation_map[right]:
            # higher point found
            if elevation_map[left] > e1:
                e1 = elevation_map[left]
            # there could be water
            else:
                volume += e1 - elevation_map[left]
            left += 1
        else:
            # higher point found
            if elevation_map[right] > e2:
                e2 = elevation_map[right]
            # there could be water
            else:
                volume += e2 - elevation_map[right]
            right -= 1

    return volume

elevation_map_1 = [0,1,0,2,1,0,1,3,2,1,2,1]
elevation_map_2 = [4,2,0,3,2,5]
elevation_map_3 = [2, 0, 1]

assert calculate_water_volume(elevation_map_1) == 6
assert calculate_water_volume(elevation_map_2) == 9
assert calculate_water_volume(elevation_map_3) == 1

print("all tests passed.")