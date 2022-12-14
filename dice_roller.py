import random

def main():
    dice_rolls: int = int(input('How many dice would you like to roll? '))
    dice_size = int(input('How many sides are the dice?'))
    dice_sum: int = 0
    for _ in range(dice_rolls):
        roll: int = random.randint(1, dice_size)
        dice_sum += roll
        if roll == 1:
            print('You rolled a 1! Critical Fail')
        elif roll == dice_size:
            print(f'You rolled a {dice_size}! Critical Success!')
        else:
            print(f'You rolled a {roll}')
    print(f'You have rolled a total of {dice_sum}')

if __name__ == "__main__":
    main()