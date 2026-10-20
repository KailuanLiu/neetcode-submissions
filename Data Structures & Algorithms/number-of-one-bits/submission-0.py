class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_string = bin(n)
        bin_int = list(bin_string)
        count = 0
        for b in bin_int:
            if b == "1":
                count += 1
        return count
