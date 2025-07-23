class Solution:
    def maximumGain(self, s, x, y):
        ans = 0
        if y > x:
            top = "ba"
            top_score = y
            bot = "ab"
            bot_score = x
        else:
            top = "ab"
            top_score = x
            bot = "ba"
            bot_score = y

   
        stack = []
        for i in s:
            if i == top[1] and stack  and stack[-1] == top[0]:
                ans += top_score
                stack.pop()  
            else:
                stack.append(i)

       
        new_stack = []
        for i in stack:
            if i == bot[1] and new_stack and new_stack[-1] == bot[0]:
                ans += bot_score
                new_stack.pop()
            else:
                new_stack.append(i)

        return ans
    
