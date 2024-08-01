The "Island Perimeter" problem is a common coding challenge that involves determining the perimeter of an island in a grid. The grid is represented by a 2D array where each cell is either land (1) or water (0). The goal is to calculate the perimeter of the island, which is defined as the total length of the land cells' edges that are not shared with another land cell.

### Problem Statement
Given a grid of size `n x m` consisting of 0s (water) and 1s (land), calculate the perimeter of the island. The island is formed by connected 1s (land cells) and is surrounded by water. You may assume that all four edges of the grid are surrounded by water.

### Example
```plaintext
Input:
grid = [
  [0, 1, 0, 0],
  [1, 1, 1, 0],
  [0, 1, 0, 0],
  [1, 1, 0, 0]
]

Output: 16
```

### Explanation
In the given grid, the island perimeter is 16. Each land cell contributes to the perimeter as follows:
- The cell at (0, 1) contributes 4 to the perimeter (it's an isolated land cell).
- The cell at (1, 0) contributes 3 to the perimeter (one side touches another land cell).
- The cell at (1, 1) contributes 2 to the perimeter (it has two neighboring land cells).
- The cell at (1, 2) contributes 3 to the perimeter (one side touches another land cell).
- The cell at (2, 1) contributes 3 to the perimeter (one side touches another land cell).
- The cell at (3, 0) contributes 3 to the perimeter (one side touches another land cell).
- The cell at (3, 1) contributes 2 to the perimeter (it has two neighboring land cells).

### Approach
1. **Iterate through each cell in the grid**:
   - If the cell is land (1), add 4 to the perimeter count.
   - Check for neighboring land cells (top, bottom, left, right). For each neighboring land cell, subtract 1 from the perimeter count (since that side is not a part of the perimeter anymore).

### Implementation in Python
Here's a Python implementation of the algorithm:

```python
def island_perimeter(grid):
    if not grid:
        return 0
    
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4
                if r > 0 and grid[r - 1][c] == 1:  # check above
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:  # check left
                    perimeter -= 2
    
    return perimeter

# Example usage
grid = [
  [0, 1, 0, 0],
  [1, 1, 1, 0],
  [0, 1, 0, 0],
  [1, 1, 0, 0]
]

print(island_perimeter(grid))  # Output: 16
```

### Key Points
- Each land cell contributes 4 to the perimeter initially.
- Shared edges with other land cells reduce the perimeter by 2 for each shared edge (since each side is counted twice).

This problem helps to understand the concepts of grid traversal and boundary conditions.
