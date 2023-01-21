import re

def LongestWord(str):
    key = "ufec01234ded"
    str =str.replace('&'," ")
    str =str.replace('!'," ")
    nlist = str.split(' ')
    max_len = 0
    ans =""
    for i in nlist:
        if len(i) >= max_len:
            max_len = len(i)
            ans = i
    ans = ans+key
    for i  in range(1,len(ans)):
        if i%4 == 0 and i!=0:
            ans = ans.replace(ans[i],"_")
    return ans



print(LongestWord('fun&!! time'))