
# WAY 1:
# from random import randint

# weekly_draw = []
# while len(weekly_draw) < 7:
#     new_rnd = randint(1,40)
#     if new_rnd not in weekly_draw:
#         weekly_draw.append(new_rnd)

# print(weekly_draw)


# WAY2:
# from random import shuffle

# number_pool = list(range(1, 41))
# shuffle(number_pool)
# weekly_draw = number_pool[0:7]
# print(weekly_draw)


# WAY 3:
# from random import sample

# number_pool = list(range(1, 41))
# weekly_draw = sample(number_pool, 7)
# print(weekly_draw)