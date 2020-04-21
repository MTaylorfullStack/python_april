import random

random_number = round(random.random() * 10)
print(random_number)

# Task One: Familiarize Ourselves w/ The Data and 'random' Library

players = [
    {
        'name': 'Ed',
        'score': 0,
        'attempts': 0,
        'previous_guesses': []
    },
    {
        'name': 'Tobin',
        'score': 0,
        'attempts': 0,
        'previous_guesses': []
    },
    {
        'name': 'Raj',
        'score': 0,
        'attempts': 0,
        'previous_guesses': []
    },
    {
        'name': 'MonaLisa',
        'score': 0,
        'attempts': 0,
        'previous_guesses': []
    },
    {
        'name': 'Sheetal',
        'score': 0,
        'attempts': 0,
        'previous_guesses': []
    }
]

# Task Two: Write a function that accepts a player object and a number guess
    # if guess is within 10 integers of generated number, score += 10
    # if guess is within 5 integers of generated number, score += 30
    # if guess is equal to generated number, score += 50

    # guesses are tracked for player
    # previous_guesses is tracked for player


# declare function, take player and number as parameters
    # create our random number
    # if number<rand_num+10 or number>rand_num-10:
        # in bounds, player gains 10 points
    # if number<rand_num+5 or number>rand_num-5:
        # in bounds, player gains 30 points
    # if number == rand_num
        # player gains 50 points
    # track guess number
    # track guess count



def random_number_game(player, guess):
    rand_num = round(random.random() * 50)
    if guess == rand_num:
        print(f"{player['name']} has guessed the number {rand_num}!!!")
        player['score'] += 50
    player['attempts'] += 1
    player['previous_guesses'].append(guess)
    print(f"Starting conditionals, guess is: {guess}, rand_num is: {rand_num}")
    ten_less = rand_num-10
    ten_more = rand_num+10
    range_list = []
    for num in range(ten_less, ten_more+1):
        range_list.append(num)
    print(range_list, "This is range list")
    # if guess<rand_num-10 or guess>rand_num+10:
    #     print(f"{player['name']} has guessed within 10 of the target {rand_num}!")
    #     player['score'] += 10
    # elif guess<rand_num-5 or guess>rand_num+5:
    #     print(f"{player['name']} has guessed within 5 of the target {rand_num}!")
    #     player['score'] += 30
    # elif guess==rand_num:
    #     print(f"{player['name']} has guessed the number {rand_num}!!!")
    #     player['score'] += 50
    if guess in range_list:
        for num in range(5, 16):
            if(range_list[num] == guess):
                print(f"{player['name']} has guessed within 5 of the target {rand_num}!")
                player['score'] += 30
        print(f"{player['name']} has guessed within 10 of the target {rand_num}!")
        player['score'] += 10
    return player


# for index in range(len(players)):
#     for guess in range(5, 25):
#         print(f"Result: {random_number_game(players[index], guess)}")

# print(f"This is my final product {players}")

random_number_game(players[0], 10)


    



