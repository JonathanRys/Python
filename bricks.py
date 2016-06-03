#!/usr/bin/python

from fractions import gcd
from functools import reduce
from collections import deque
from collections import defaultdict
 
#finds the least common multiple(LCM) of two numbers
def lcm(nums):
    return reduce(lambda x, y: (x*y)/gcd(x,y), nums, 1)
 
#adds all elements in an array or list
def row_sum(row):
    return reduce(lambda x, y: x+y, row, 0)
 
#removes smaller bricks and adds the smallest set of larger ones
def grow_bricks(ary, max_width):
    ary.sort()

    q = deque(ary)
    tmp = 0
    while tmp < divisor:
        tmp += q.popleft()
        if(row_sum(q) + bricks[-1] <= max_width):
            q.extend([bricks[-1]])
    return q

def smallest_row(width):
    smallest_array = []
    
    #build the row with the most bricks first
    while row_sum(smallest_array) < width:
        smallest_array.append(bricks[0])
    
    while row_sum(smallest_array) > width:
        smallest_array.pop()
        smallest_array.pop()
        smallest_array.append(bricks[-1])
    return smallest_array
 
#build a list containing all possible combos for a single layer
def first_row(width):
    #start building the possible layers
    global permutations
    bricks.sort()
    min_per_row = width // bricks[-1]
    walls = []
    count = 0

    base_array = smallest_row(width)
    if len(base_array) <= 2:
        if base_array == base_array.reverse():
            return [base_array]
        else:
            walls.append(base_array)
            walls.append(sorted(base_array))
            return walls
    
    #no need to permute the first row
    walls.append(base_array)

    #calculate all permutations
    while len(base_array) > min_per_row:
        base_array = list(grow_bricks(base_array, width))
        if row_sum(base_array) != width: continue
        permutations = []
        permute(base_array)
        walls = walls + permutations

    return walls

#find all permutations for a layer
def permute(ary):
    permute_helper(ary, 0)
 
def permute_helper(arr, index):
    #nothing left to permute
    if index >= len(arr) - 1:       
        if arr not in permutations:
            permutations.append(list(arr))
            return arr
   
    for i in range(index, len(arr)):
        #swap elements at index and i
        tmp = arr[index]
        arr[index] = arr[i]
        arr[i] = tmp
 
        #recurse on the sub-list
        permute_helper(arr, index + 1)
 
        #swap the elements back
        tmp = arr[index]
        arr[index] = arr[i]
        arr[i] = tmp

#find where the mortar seams are in the layer
def get_seams(bricks, width):
    mortar_seams = []
    for x in bricks:
        #build a list of seams for this row
        mortar_seams.append([])
        running_count = 0
        for i in x:
            running_count += i
            mortar_seams[bricks.index(x)].append(running_count)

    return mortar_seams

#compare seams to find which ones stack
def compare(seams):
    brick_map = []
    for x in seams:
        for y in seams:
            if x == y: continue
            counter = 0
            for i in y:
                if i in x:
                    break
                counter += 1
            if counter + 1 == len(y):
                brick_map.append([seams.index(x), seams.index(y)])
    return brick_map

def list_to_dict(my_list):
    d = defaultdict(list)
 
    for i, j in my_list:
        d[i].append(j)
    return d

def follow_map(lookup, new_map):
    brick_map = []
    for i in new_map:
        for j in lookup[i]:
            brick_map.append(j)
    #brick_map.append(len(brick_map))
    return brick_map

def print_layers(rows, width):
    #print a visual representation of the rows
    print("Possible layers:")
    print(" ", end="")
    for i in range(2, int(width * 2)):
        print("_", end="")
    print(" ")

    #make this dynamic
    for i in rows:
        for j in i:
            if j == bricks[0]:
                print("|" + "_" * int(bricks[0] * 2 - 2) + "|", end="")
            else:
                print("|" + "_" * int(bricks[1] * 2 - 2) + "|", end="")
        print("")
    print("")

#build all possible walls and report the results
def build_wall(wall_width, wall_height):
    print("\nBuilding a", wall_width, "x", wall_height, "wall using the following bricks:", bricks)

    #find the ways to build a single layer
    brick_rows = first_row(wall_width)

    #print out the different layers
    print_layers(brick_rows, wall_width)

    #find the seams in each valid layer
    last_seams = get_seams(brick_rows, wall_width)

    #create a map of which layers will stack on which
    my_map = compare(last_seams)
    
    lookup_table = list_to_dict(my_map)
    new_map = [x[1] for x in my_map]
    map_len = len(brick_rows)

    #calculate all the combinations
    for i in range(1, int(wall_height)):
        map_len = len(new_map)
        new_map = follow_map(lookup_table, new_map)        
    
    #report results
    print(map_len, "possible walls")

def validate_width(w):
    if w == row_sum(bricks): return True
    
    for i in bricks:
        if w % i == 0 or w % i == bricks[bricks.index(i) - 1]:
            continue
        return False
    return True

##### MAIN PROGRAM CODE #####
bricks = [3, 4.5]
divisor = lcm(bricks)
permutations = []
last_tier = 0

#collect input  
input_width = float(input("Enter width of wall: "))

while not validate_width(input_width):
    print("Invalid width.\nUsing the following bricks:", bricks)
    input_width = float(input("Enter width of wall: "))

input_height = float(input("Enter height of wall: "))

build_wall(input_width, input_height)
