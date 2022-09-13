def love():
    def fun():
        s=[[0],[1,3],[5,7],[9,11],[13,15,7]]
        i=0
        while i<len(s):
            j=0
            small=0
            lar=0
            p=[]
            while j<len(s[i]):
                if len(s[i])>len(s[j]):
                    lar=s[i]
                if len(s[i])<len(s[j]):
                    small=s[j]
                j=j+1
            p.append(small)
            i=i+1
        print(lar,"maximum list")
        print(p,"minimum list")
    fun()
love()



# # output  
# # [13,15,7] maximum list    
# # [0] minimum list
