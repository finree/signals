print("THE DIAMOND EXPERT SYSTEM")

question1 = input("Does it float in water?")
if question1 == "Y":
    print("Diamond is fake")
else:
    question2 = input("Can it scratch glass?")
    if question2 == "N":
        print("Diamond is fake")
    else:
        question3 = input("Conduct electricity?")
        if question3 == "Y":
            print("Diamond is fake")
        else:
            print("Diamond could be real")
