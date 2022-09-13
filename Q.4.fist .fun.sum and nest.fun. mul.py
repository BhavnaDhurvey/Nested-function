def sum(list):
    i=0
    sum=0
    while i<len(list):
        sum=sum+list[i]
        i=i+1
    return sum 
list=[2,4,6,8,9]
b=sum(list)
print(b)
def mul(b):
    c=b*2
    return c
d=mul(b)
print(d)