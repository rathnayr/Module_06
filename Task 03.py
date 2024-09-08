def gallon_to_liter (gallons):
    Liters=gallons * 3.78541
    return Liters

def main():
    while True:
        gallons= float (input("Enter the quantity in gallons: "))

        if gallons<0:
            print("Please enter a positive value")
            break

        Liters = gallon_to_liter (gallons)
        print (f"{gallons} gallons equal to {Liters:.2f} liters.")
main()


