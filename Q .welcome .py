def good():
    def greet(*names):
        for name in names:
            print("welcome",name)
    greet("rinki","vishal","kartik","bijender")
good()


# output
# Welcome rinki    
# Welcome vishal   
# Welcome kartik     
# Welcome bijender