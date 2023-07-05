first_name = input("Enter First name: ")
last_name = input("Enter Last name: ")

if first_name == " ":
 breakpoint(print("This space cannot be empty"))
if last_name == " ":
 breakpoint(print("This space cannot be empty"))

if first_name and last_name == first_name and last_name:
 print("Your name is ", first_name, last_name)

age = input("Enter Age: ")
if age < "0":
 print("Your age can't be negative")

if age >= "18":
    print("You are a youth", age)
if age < "18":
    print("You are underage", age)
if age > "65":
    print("You are an old citizen")
