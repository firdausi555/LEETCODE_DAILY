class Solution:
    def doesAliceWin(self, s: str) -> bool:
        lst=['a','e','i','o','u']
        for i in s :
            if i in lst:
                return True
        return False 
