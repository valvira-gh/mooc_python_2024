# completed
from random import shuffle


def lottery_numbers(amount: int, lower: int, upper: int) -> list:
    number_pool = list(range(lower, upper + 1))
    shuffle(number_pool)
    lottery_draw = sorted(number_pool[0:amount-1])

    return lottery_draw

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)
