def show ():
    def fun():
        numbers = [3, 5, 7, 34, 2, 89, 2, 5]
        i=0
        lar=numbers[0]
        while i<len(numbers):
            if numbers[i]>lar:
                lar=numbers[i]
            i=i+1
        print("maxcimum",lar)
    fun()
show ()

