def fun():
    def add_number_list():
        a= [50, 60, 10]
        b= [10, 20, 13] 
        i=0
        while i<len(a):
            c=a[i]+b[i]
            i=i+1
            print(c)
    add_number_list()
fun()



# output    
# 60
# 80
# 23