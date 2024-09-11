class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # XOR the start and goal to find differing bits
        diff = start ^ goal
        # Count the number of 1s in the binary representation of diff
        return bin(diff).count('1')
