maximum_stores = 60
usernum = int(input("On what floor of the building is your office?"))

while (usernum > maximum_stores):
    print("you entered " + str(usernum) + "but there are only" + str(maximum_stores) + "floors in the building.. try again" )
usernum = int(input("On what floor of the building is your office?"))
print("congrats you work on floor" + usernum)

