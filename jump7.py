for i in range(1,101):
    if i%7==0:
        continue
    a=i//100
    if a==7:
        continue
    b=(i-a*100)//10
    if b==7:
        continue
    c=i-a*100-b*10
    if c==7:
        continue
    print(i)
