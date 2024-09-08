import random
def roll_dice():
    return random.randint(1,6)

def main():
    roll_output=0
    while roll_output != 6:
        roll_output = roll_dice()
        print(f"Results of each roll: {roll_output}")
main()

