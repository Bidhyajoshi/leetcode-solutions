class Solution(object):
    def largestAltitude(self, gain):
        current = 0
        Highest = 0

        for g in gain:
            current = current + g

            if (current > Highest):
                Highest = current
        return Highest

gain = [-5, 1, 5, 0, -7]
obj = Solution()
print(obj.largestAltitude(gain))               

       