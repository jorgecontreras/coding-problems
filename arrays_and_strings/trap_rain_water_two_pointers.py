# trap rain water O(1)
# use two pointers

#        #
#    #   ## #
# _#_##_######

def calculate_water_volume(elevation_map):
    volume = 0
    p1 = p2 = 0
    l = 0
    r = len(elevation_map)-1

    while l < r:
        if elevation_map[l] < elevation_map[r]:
            if elevation_map[l] > p1:
                p1 = elevation_map[l]
            else:
                volume += p1 - elevation_map[l]
            l+= 1
        else:
            if elevation_map[r] > p2:
                p2 = elevation_map[r]
            else:
                volume += p2 - elevation_map[r]
            r -= 1

    return volume






elevation_map_1 = [0,1,0,2,1,0,1,3,2,1,2,1]
elevation_map_2 = [4,2,0,3,2,5]

assert calculate_water_volume(elevation_map_1) == 6
assert calculate_water_volume(elevation_map_2) == 9

