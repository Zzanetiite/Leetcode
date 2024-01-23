class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        # Convert the number to binary
        binary_num = bin(n)
        # Count the number of 1s in the binary
        for i in binary_num:
            if i == '1':
                count += 1
        # Return the count
        return count

    def hammingWeightfaster(self, n: int) -> int:
        bin(n).count('1')


n: int = 11
result = Solution().hammingWeight(n=n)
print(result)
