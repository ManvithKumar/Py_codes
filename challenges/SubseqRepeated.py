str = "PROFFESSIONALL"
n_str=""
for i in range(len(str)):
    if str[i]==str[i-1]:
        continue;
    else:
        n_str+=str[i]
print(n_str)