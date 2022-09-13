
def mom():
    def checkConsecutive(l):
        return sorted(l)==list(range(min(l),max(l) +1))
    lst = [-5,-6,-7,-8]
    print(checkConsecutive(lst))
mom()


# O/P                 
# True
