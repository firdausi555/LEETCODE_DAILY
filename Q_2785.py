class Solution:
    def sortVowels(self, s: str) -> str:
        lst=list(s)
        vol=[i for i in lst if i in "AEIOUaeiou"]
        if vol == []:
            return s

        vol.sort()

        j=0
        for i in range(len(lst)):
            if lst[i] in "AEIOUaeiou":
                lst[i]=vol[j]
                j+=1
        return "".join(lst)
