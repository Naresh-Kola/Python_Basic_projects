# import random
# define a function to roll the dice
# create a dictionary that will have the drawings of the dice

import random
from PIL import Image

dict_a = {
    1: "10_Dice_Rolling/image1.png",
    2: "10_Dice_Rolling/image2.png",
    3: "10_Dice_Rolling/image3.png",
    4: "10_Dice_Rolling/image4.png",
    5: "10_Dice_Rolling/image6.png",
    6: "10_Dice_Rolling/image6.png"
}

def roll_dice():
    roll = input("Roll the dice? (Yes/No): ")
    while roll.lower() == "yes":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("Dice rolled: {} and {}".format(dice1, dice2))

        img1 = Image.open(dict_a[dice1])
        img2 = Image.open(dict_a[dice2])

        img1.show()
        img2.show()

        roll = input("Roll again? (Yes/No): ")

roll_dice()
