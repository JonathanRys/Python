smallPyramid = [[75],
                [95, 64],
                [17, 47, 82],
                [18, 35, 87, 10],
                [20,  4, 82, 47, 65],
                [19,  1, 23, 75,  3, 34],
                [88,  2, 77, 73,  7, 63, 67],
                [99, 65,  4, 28,  6, 16, 70, 92],
                [41, 41, 26, 56, 83, 40, 80, 70, 33],
                [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
                [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
                [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
                [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
                [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
                [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]

def pathSum(pyramid):
    # Reverse the pyramid
    pyramid.reverse()
    # Initialize ghost
    ghost=[0]
    for x in pyramid[0]:
        ghost.append(0)
    # Loop through the pyramid rows
    for x in range(len(pyramid)):
        # Loop through the pyramid columns
        for y in range(len(pyramid[x])):
            # If this isn't the last column...
            if y < len(pyramid[x]) - 1:
                # If this is the first (last) row of the pyramid...
                if x == 0:
                    ghost[y] = pyramid[x + 1][y] + max([pyramid[x][y], pyramid[x][y + 1]])
                else:
                    ghost[y] = pyramid[x + 1][y] + max([ghost[y], ghost[y + 1]])
        # Remove the unused column
        ghost.pop()
    return ghost[0]
print(pathSum(smallPyramid))
