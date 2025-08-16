class Solution:
    def maximum69Number (self, num: int) -> int:
        result =0
        iterable=list(str(num))
        for i in range(len(iterable)):
            temp=list(str(num))
            if iterable[i]=='6':
                temp[i]="9"
            i_temp=int("".join(temp))
            if i_temp>result:
                result=i_temp
        return result
