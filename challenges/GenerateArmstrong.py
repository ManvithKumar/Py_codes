print("Armstrong Numbers Between 1 and 1000:")
first = 1
last = 1000
while first<=last:
  res = 0
  temp = first
  noOfDigit = 0
  while temp>0:
    temp = int(temp/10)
    noOfDigit = noOfDigit + 1
  num = first
  while num>0:
    rem = num%10
    pow = 1
    i = 0
    while i<noOfDigit:
      pow = pow*rem
      i = i+1
    res = res+pow
    num = int(num/10)
  if res == first:
    print(res)
  first = first+1