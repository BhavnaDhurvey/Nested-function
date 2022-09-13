def max(list):
    i=0
    l=list[0]
    while i<len(list):
        if list[i]>l:
            l=list[i]
        i=i+1
    return l         
list=[1,5,6,8,2]
a=max(list)
print(a)
