def sum():
    def num():
        a=int(input("enter the number..."))
        i=1
        sum=0
        while i<=a:
            if i%3==0 or i%5==0:
                print(i) 
                sum=sum+i
            i=i+1
        print(sum) 
    num() 
sum()
      