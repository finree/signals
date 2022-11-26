age = int(input("Enter your age: "))
if age < 25:
    print("High")
else:
    type_car = input("Type of car: Fast car, Family car (fast/family)")
    if type_car == "fam":
        print("Low")
    else:
        car_accicent = input("Have you had an accident?: (y/n)")
        if car_accicent == "n":
            print("Medium")
        else:
            print("High")