def num():
    def fun(list):
        D=int(input("enter the number..."))
        i=D
        while i>0:
            print(list[-i])
            i=i-1
    fun( ['a', 1, '2', 5, 'b', 'q'])
num()

# input   
# 2  , 3
# output   
# b  ,5   
# q  ,b 
  #  ,q
