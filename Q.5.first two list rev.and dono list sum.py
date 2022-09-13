def sum(list,list1):
    i=-1
    a=[]
    b=[]
    while i >=-len(list):
        a.append(list[i])
        b.append(list1[i])
        i=i-1
    print(a)
    print(b)
    i=0
    c=[]
    while i<len(a):
        s=a[i]+b[i]
        c.append(s)
        i=i+1
    print(c)
list=[1,2,3,4]
list1=[5,6,7,8]
sum(list,list1)
