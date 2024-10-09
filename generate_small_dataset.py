import numpy as np
import sys
import random

def main():
    subsets, total = CreateSubsets(int(sys.argv[1]))

    with open(sys.argv[2], 'w') as file:
        for i, subset in enumerate(subsets):
            for j, count in enumerate(subset):
                random_number = random.randint(1, 100)
                file.write(f"{i+1} {j+1} {random_number} 0.0001\n")

    print(total)


def CreateSubsets(node_count):

    grid_size = int(np.ceil(np.sqrt(node_count)))

    # Initialize grid to form subsets
    grid = np.arange(1, grid_size**2 + 1).reshape(grid_size, grid_size)

    # Remove any nodes outside the original
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] > node_count:
                grid[i][j] = -1
    
    subsets = []
    count = 1
    total = 0
    # Generate the subsets from the row column union
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == -1:
                continue
            row = grid[i,:]
            col = grid[:,j]
            subset = set(row) | set(col)

            # Remove the -1's indicating no entries
            if (-1 in subset):
                subset.remove(-1)
            
            subset = [int(x) for x in subset]
            count += 1
            subsets.append(subset)
            total += len(subset)

    for subset in subsets:
        print(subset)
    return subsets, total

if __name__ == "__main__":
    main()