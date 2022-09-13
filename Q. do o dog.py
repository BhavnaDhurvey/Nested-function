def dip():
    def fun():
        a="dog"
        i=0
        b=[]
        while i<len(a):
            j=i+1
            while j<=len(a):
                c=a[i:j]
                b.append(c)
                j=j+1
            i=i+1
        print(b)
    fun()
dip()