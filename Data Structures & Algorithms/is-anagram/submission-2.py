class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        if len(s) == 0 and len(t) == 0:
            return False

        # this creates hashmap : ) 
        count_string = Counter(s)

        # iterate through t and decrement count 
        for c in t:
            count_string[c] -= 1 
            if count_string[c] < 0:
                return False
        return True