class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        row = rows - 1  # Start from the last row
        col = 0  # Start from the first column

        while row >= 0 and col < cols:
            if grid[row][col] < 0:
                count += cols - col
                row -= 1  # Move to the previous row
            else:
                col += 1  # Move to the next column

        return count
