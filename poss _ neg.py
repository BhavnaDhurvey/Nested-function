def dad():
    def pos_neg():
        list = [2, -7, 5, -64, -14]
        i=0
        pos=0
        neg=0
        while i<len(list):
            if list[i]>=0:
               pos=pos+1
            else:
                neg=neg+1
            i=i+1
        print("possitive numbers in the list: ", pos)
        print("nagetive numbers in the list: ", -neg)
    pos_neg()
dad()

# Output: pos = 2, neg = 3
