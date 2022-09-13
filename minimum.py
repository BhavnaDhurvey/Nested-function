def ram():
    def fun():
        list = [8, 6, 4, 8, 4, 50, 2, 7]
        small=list[0]
        i=0
        while i<len(list):
            if list[i]<small:
               small=list[i]
            i=i+1
        print("minimum",small)
    fun()
ram()
