def sad():
    def fun(age):
        if age>=21:
           return "drink whisky"
        elif age>18:
           return "drink beer"
        elif age>14:
           return "drink coke"
        elif age>13:
           return "drink toddy"
    age=int(input("enter th number.."))
    print(fun(age))
sad()