class Solution:
    def isValid(self, word: str) -> bool:
        pas=''
        countV=0
        countC=0
        vowels=['a','e','i','o','u','A','E','I','O','U']
        if len(word)<3:
            return False
        for i in word:
            if i.isalnum():
                pas=True
            else:
                return False
        for i in word:
            if i in vowels:
                countV+=1
            elif i not in vowels and 97<=ord(i)<=122 or 65<=ord(i)<=90:
                countC+=1
        if countV>=1 and countC>=1 and pas==True:
            return True
        else:
            return False
        return pas
