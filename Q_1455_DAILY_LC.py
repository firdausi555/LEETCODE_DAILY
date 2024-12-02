class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        temp=sentence.split(' ')
        for i in range(len(temp)):
            if searchWord in temp[i][0:len(searchWord)]:
                return i+1
        return -1
