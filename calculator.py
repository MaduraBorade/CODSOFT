x = float(input("ENTER FIRST NUMBER: "))
y = float(input("ENTER SECOND NUMBER: "))

print("------------------PLEASE SELECT OPTION AS PER YOUR NEED----------------------")
print("1 - ADDITION (+)")
print("2 - SUBTRACTION (-)")
print("3 - DIVISION (/)")
print("4 - MULTIPLICATION (*)")

a = input("Enter your choice (1, 2, 3, 4): ")

if a == '1':
    r = x + y
elif a == '2':
    r = x - y
elif a == '3':
    r = x / y
elif a == '4':
    r = x * y
else:
    print("Damn! You chose a wrong option.")
    exit()

print("AS PER YOUR SELCTED OPRERATION OUTPUT IS :", r)
