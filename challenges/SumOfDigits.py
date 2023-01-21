import re
import sys, re

def test(str):
    n_sum =sum([sum(map(int,re.findall(r"[0-9]{1,5}",str)))])
    return n_sum

print(test("75Number9"))