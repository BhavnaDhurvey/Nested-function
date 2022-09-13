def mom():
    def dad():
        a='The quick Brow Fox'
        i=0
        Uppercase=0
        Lowercase=0
        while i<len(a):
            if a[i].isupper():
                Uppercase+=1
            elif a[i].islower():
                Lowercase+=1
            else:
                pass
            i=i+1
        print("No. of Lower case Characters :",Lowercase)
        print("No. of Uppercase characters : ",Uppercase)
    dad()
mom()


# output  
# No. of Lower case Characters : 12
# No. of Uppercase characters : 3
