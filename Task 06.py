import math

def Unit_price_for_square_meter(diameter, price):
    Diameter_in_meters = diameter / 100
    radius = Diameter_in_meters/ 2
    Area= math.pi *(radius**2)
    Unit_price= price / Area

    return Unit_price

def main():
    diameter1 = float(input("Enter the diameter of the 1st pizza in centimeters:"))
    price1 = float(input("Enter the price of the 1st pizza in euros:"))

    diameter2 = float(input("Enter the diameter of the 2nd pizza in centimeters:"))
    price2 = float(input("Enter the price of the 2nd pizza in euros:"))

    unitPrice1 = Unit_price_for_square_meter(diameter1, price1)
    unitPrice2 = Unit_price_for_square_meter(diameter2, price1)

    print(f"First pizza unit price is: {unitPrice1:.2f} euros per square meter.")
    print(f"Second pizza unit price is: {unitPrice2:.2f} euros per square meter.")

    if unitPrice1 < unitPrice2:
        print("The first pizza provides better value for money.")

    elif unitPrice1 > unitPrice2:
        print("The second pizza provides better value for money.")

    else:
        print("Both Pizzas provide the same value for money.")

main()