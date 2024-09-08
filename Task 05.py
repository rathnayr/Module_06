def Remove_Odd_Numbers (numbers):
    Even_Number = [num for num in numbers if num % 2 == 0]
    return Even_Number

def main():
    List_of_Numbers = [1,2,3,4,5,6,7,8,9,10]

    List_of_Even_Numbers = Remove_Odd_Numbers(List_of_Numbers)

    print(f"List of Numbers provided: {List_of_Numbers}")
    print(f"List which odd numbers removed: {List_of_Even_Numbers}")

main()