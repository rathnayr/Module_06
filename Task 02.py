import random
def roll_dice(sides):
    return random.randint(1, sides)
def main():
    sides = int(input("Enter number of sides on dice: "))
    roll_output = 0
    while roll_output != sides:
        roll_output = roll_dice(sides)
        print(f"Rsults of each rolled: {roll_output}")
main()