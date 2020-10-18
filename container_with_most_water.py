# https://leetcode.com/problems/container-with-most-water/

# time complexity: O(n)
# space complexity: O(1)


class Solution:
    def maxArea(self, height: List[int]) -> int:

        leftIndex = 0
        rightIndex = len(height) - 1
        maxSeen = 0

        while leftIndex < rightIndex:
            currentContainerSize = (rightIndex - leftIndex) * min(
                height[leftIndex], height[rightIndex]
            )

            if currentContainerSize > maxSeen:
                maxSeen = currentContainerSize

            if height[leftIndex] > height[rightIndex]:
                rightIndex -= 1
            else:
                leftIndex += 1

        return maxSeen
