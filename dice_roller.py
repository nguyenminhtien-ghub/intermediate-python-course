import random

def main():
    dice_rolls: int = 2
    dice_sum: int = 0
    for _ in range(dice_rolls):
        roll: int = random.randint(1, 6)
        dice_sum += roll
        print(f'You rolled a {roll}')
    print(f'You have rolled a total of {dice_sum}')

if __name__ == "__main__":
    main()