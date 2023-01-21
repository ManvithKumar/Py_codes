def RepeatedChar(str):
    dict={}
    max_value=0
    for i in str:
        if i not in dict:
            dict[i] = 1 
        elif i in dict:
            dict[i] +=1
    
    for x,y in dict.items():
        if y > max_value :
            max_value = y
            ans = x
    return ans

str = "Hello World"
print(RepeatedChar(str))