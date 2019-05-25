age = 24
print("My age is " + str(age) + " years")
print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}".format(31, "January", "March", "May", "July", "August", "October", "December"))
print("There are {0} days in {1}, {2}, {3}, {4}".format(30, "April", "June", "September", "November"))
print("There are {0} or {1} days in Febrauary".format(28, 29))

print('''
January: {2}, 
Febrauary: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
Semtember: {1}
October: {2}
November: {1}   
December: {1}'''.format(28, 30, 31))

print("My age is %d years" %age)
print("My age is %d %s %d %s" % (age, "years", 6, "months"))

for i in range(1, 12):
    print("No. %2d squared is %3d and cubed is %4d" % (i, i ** 2, i ** 3))

print("pi of aproximately %12.50f" % (22 / 7))

for i in range(1, 12):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print("pi of aproximately {0:.5}".format(22 / 7))