class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        water = 0

        idx_left = 0
        idx_right = len(height) - 1
        left_max = 0
        right_max = 0

        while idx_left < idx_right:
            if height[idx_left] < height[idx_right]:
                if height[idx_left] >= left_max:
                    left_max = height[idx_left]
                else:
                    # there's space between left_max and right_max, so add it
                    water += left_max - height[idx_left]
                # move right
                idx_left += 1

            else:
                if height[idx_right] >= right_max:
                    right_max = height[idx_right]
                else:
                    # there's space between left_max and right_max, so add it
                    water += right_max - height[idx_right]
                # move left
                idx_right -= 1

        return water
