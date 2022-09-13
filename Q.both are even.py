def very():
    def check_number_list():
        a=[2, 6, 18, 10, 3, 75]
        b=[6, 19, 24, 12, 3, 87] 
        i=0
        while i<len(a) and len(b):
            if a[i]%2==0 and b[i]%2==0:
               print("both are even")
            else:
                print("both are not even")
                
            i=i+1
                
    check_number_list()
very()



# output   
# both are even
# both are not even
# both are even
# both are not even
# both are not even
