class Solution:
    def removeSubfolders(self, folder):
        folder.sort()
        ans=[]
        for i in folder:
            if not ans or not i.startswith(ans[-1]+'/'):
                ans.append(i)

        return ans 
