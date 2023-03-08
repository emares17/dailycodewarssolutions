# LeetCode 



# ------------------------------------Solution-------------------------------------

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        return count

# Or-------------------------------------------------------------------------------

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dicti = {}
        for stone in stones:
            dicti[stone] = dicti.get(stone, 0) + 1
        
        count = 0
        for k,v in dicti.items():
            if k in jewels:
                count += v
        
        return count