gallons = float(input('Enter the number of gallons used: '))
miles = float(input("Miles driven: "))

mileage = 0.0
count = 0
while gallons != -1:
    count += 1
    mileage += (miles / gallons)
    semi_total = miles / gallons
    grand_total = mileage / count
    gallons = float(input("Enter the gallons used: "))
    miles = float(input('Miles driven:'))
    print("The miles/gallon for this tank was ", semi_total)
    if gallons == -1:
        print("The overall average miles/gallon was ", grand_total)
