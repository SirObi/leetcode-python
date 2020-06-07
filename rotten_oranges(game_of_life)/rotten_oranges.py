class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])

        if height == 0 or width == 0:
            return -1

        minutes = 0
        n_fresh_oranges = 0
        to_rot = []

        # on first pass, find all rotten oranges, add adjacent to queue for rotting (unless empty)
        # find number of all remaining fresh oranges
        while True:
            for i in range(height):
                for j in range(width):
                    if grid[i][j] == 2:
                        top = (i - 1, j) if i - 1 >= 0 else None
                        bottom = (i + 1, j) if i + 1 <= height - 1 else None
                        left = (i, j - 1) if j - 1 >= 0 else None
                        right = (i, j + 1) if j + 1 <= width - 1 else None

                        fields = (n for n in [top, bottom, left, right] if n)
                        fresh = (f for f in fields if grid[f[0]][f[1]] == 1)
                        to_rot += [o for o in fresh]

                    if grid[i][j] == 1:
                        n_fresh_oranges += 1

            if len(to_rot) == 0 and n_fresh_oranges > 0:
                return - 1

            elif len(to_rot) == 0 and n_fresh_oranges == 0:
                return minutes

            # Clean queue and update state one by one
            for i in range(len(to_rot)):
                i,j = to_rot.pop()
                grid[i][j] = 2
            n_fresh_oranges = 0

            minutes += 1



# DANGEROUS!! - use in range(len()) instead
#for coord_pair in to_rot:
#   i,j = to_rot.pop()
#   grid[i][j] = 2

# This exercise is a variation of https://leetcode.com/discuss/interview-question/411357/
# there's just one more condition (<= there can be oranges that are inaccessible)

# Link: https://leetcode.com/submissions/detail/350420795/
