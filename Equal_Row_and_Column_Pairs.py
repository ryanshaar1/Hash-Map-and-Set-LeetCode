class Solution(object):
    def equalPairs(self, grid):
        columns = [[] for _ in range(len(grid[0]))]
        for i in range(len(grid[0])):
            for j in range(len(grid[0])):
                columns[i].append(grid[j][i])
        
        count = 0
        for row in grid:
            for column in columns:
                if row == column:
                    count += 1
        return count
