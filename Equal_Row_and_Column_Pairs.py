from collections import Counter

class Solution:
    def equalPairs(self, grid):
        row_count = Counter(tuple(row) for row in grid)
        
        count = 0
        for col_idx in range(len(grid[0])):
            column = tuple(grid[row_idx][col_idx] for row_idx in range(len(grid)))
            count += row_count[column]
        
        return count
