
def fun (list):
    i=-1
    a=[]
    while i>=-len(list):
        a.append(list[i])
        i=i-1
    return a
list=[1,2,3,4,5]
z=fun(list)
print(z)