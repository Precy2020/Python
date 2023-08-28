def hello_name():
    userName = input("Enter your name: ")
    if userName.isdigit():
        print("Invalid Name")
        hello_name()
    else:
        print("Hello ", userName)


hello_name()
