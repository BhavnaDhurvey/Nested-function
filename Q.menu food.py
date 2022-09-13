def fun():
    def menu(day):
        if day  == "monday":
           food =  "Butter chicken"
        elif day == "tuesday":
            food = "Mutton Chaap"
        else: 
            food = "Chole bhature"
        print("Will I be able to print? :-(")
        return   food
    print("But I`m not sure will print? :`)")
    print(menu("monday"))
fun()


# Output :-

# Will I be able to print? :-(
# Butter Chicken