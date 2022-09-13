def perfect():
    def fun(n):
        sum=0
        i=1
        while i<n:
            if n%i==0:
                sum=sum+i
            i=i+1
        if n==sum:
            return "it is perfect"
        else:
            return "it is not perfect"
    n=int(input("enter the number...."))
    print(fun(n))
perfect()
