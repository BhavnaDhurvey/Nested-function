# def fun():
#   print("no")
#   fun()
# fun()

i=0
def fun():
    global i
    i=i+1
    print("hello",i)
    fun()
fun()


# i=0
# def fun():
#     i=0
#     i=i+1
#     print("hello",i)
#     fun()
# fun()


# import sys
# print(sys.getrecursionlimit())


# def fun():
#   print("no")
#   div() 
# def div():
#     print("ko")
# fun()

