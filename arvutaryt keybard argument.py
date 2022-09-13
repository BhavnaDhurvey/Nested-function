# def fun(a,**b):
#     print(a)
#     for i,j in b.items():
#         print (i,j)
# fun(5,mol=56789,city="MP")




def fun(**name):
    print(**name)
name="hi","ho","lo"
fun(name)