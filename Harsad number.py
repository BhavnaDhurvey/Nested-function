def fun():
    def ram():
        s=int(input("enter the number...."))
        p=s
        rem=0
        sum=0
        while p>0:
            rem=s%10
            sum=sum+rem
            p=p//10
        if s%sum==0:
            print("this is harsad number")
        else:
            print("this is not harsad number")
    ram()
fun()


# input  6 
# output = this is harshad number