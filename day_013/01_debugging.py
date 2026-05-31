# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You've got it!")
#
# my_function()

from random import randint
dice_images = ["-1-", "-2-", "-3-", "-4-", "-5-", "-6-"]
# dice_num = randint(1, 6)
dice_num = randint(0, 5)
# Error
print(dice_images[dice_num])
