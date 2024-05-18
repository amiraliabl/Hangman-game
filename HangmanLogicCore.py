sports = [
    "Soccer", "Basketball", "Tennis", "Baseball", "Golf",
    "Volleyball", "Badminton", "Swimming", "Boxing", "Skiing",
    "Cricket", "Rugby", "Surfing", "Cycling", "Fencing",
    "Karate", "Judo", "Taekwondo", "Wrestling", "Squash"
]

films_series = [
    "Titanic", "Inception", "Gladiator", "Braveheart", "Matrix",
    "Avatar", "Incredibles", "Jaws", "Rocky", "Godfather",
    "Friends", "Lost", "Sherlock", "Vikings", "Narcos",
    "Stranger Things", "Breaking Bad", "The Crown", "The Mandalorian",
    "The Witcher", "Peaky blinders", "Breaking bad", "Game of Thrones"
]

video_games = [
    "Minecraft", "Fortnite", "Overwatch", "Halo", "Tetris",
    "Pac-Man", "Skyrim", "Zelda", "Mario", "Sonic",
    "Doom", "Fallout", "Witcher", "Cyberpunk", "Red Dead Redemption",
    "Assassin’s Creed", "Call of Duty", "Battlefield", "Dark Souls",
    "Bloodborne", "Pubg mobile"
]

food = [
    "Pizza", "Burger", "Sushi", "Pasta", "Salad", "Sandwich",
    "Tacos", "Curry", "Dumplings", "Paella", "Lasagna", "Ramen",
    "Steak", "Barbecue", "Falafel", "Goulash", "Risotto", "Tapas",
    "Kebab", "Pancake"
]

fruit = [
    "Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig",
    "Grape", "Honeydew", "Jackfruit", "Kiwi", "Lemon", "Mango",
    "Nectarine", "Orange", "Papaya", "Quince", "Raspberry",
    "Strawberry", "Tangerine", "Ugli Fruit"
]



from random import choice
while True:
    category = input('''please select your category from
    sport,film/series,food,fruit, video game : ''')
    guessed_letter = []
    if category in 'sport':
        word = choice(sports).lower()
    elif category in 'film/series':
        word = choice(films_series).lower()
    elif category in 'food':
        word = choice(food).lower()
    elif category in 'fruit':
        word = choice(fruit).lower()
    elif category in 'video game':
        word = choice(fruit).lower()
    else:
        print('please enter valid category')
        word = None



    blank = ['-']*len(word)
    print(' '.join(blank))
    chance = 6
    while chance > 0:
        correct_guess = False
        guess = input(f"let's guess... you have {chance} chance to guess the word : ")
        if guess in guessed_letter:
            print('you already guess this word')
            chance = chance-1
        elif len(guess) > 1:
            print('you should enter only one letter')
            chance = chance-1
        elif not guess.isalpha():
            print('please enter letter!!!')
            chance = chance-1
        else:

            for index, letter in enumerate(word):
                if letter == guess:
                    blank[index] = guess
                    correct_guess = True

            if correct_guess==True:
                print(' '.join(blank))

            else:
                print('incorrect guess')

            chance = chance-1
        guessed_letter.append(guess)

    if '-' not in blank:
        print('you won')
    else:
        print(f"better luck next time! the word was {word} ")
    end = input('replay or exit :')
    if end == 'replay':
        print("let's start again")
    elif end == 'exit':
        print('good luck')
        break
    else:
        print('!!!!!!!')
        break



































# for char in a:
#     blank.append('-')
#
# for i in range(7):
#     guess = input('enter : ')
#     index = 0
#     for letter in a:
#         if guess == letter:
#             blank[index] = guess
#         index += 1
#     print(' '.join(blank))
# else:
#     print('incorrect guess')










































































