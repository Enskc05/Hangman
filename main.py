
user=input("Enter your name: ")
print(f"Hello {user}. You are welcome the hangman")
print("Please select level.")
level_select = input("1-> Easy , 2-> Medium , 3-> Difficult ")
guess_string = ""
if level_select == 1:
    live = 10
    password="Metallica"
    print("İnfo:Their music is in the thrash, metal genre and they have won Grammy awards. James Hetfield and Lars Ulrich are the founding members of the band.")
    while live >0:
        character_left = 0
        for character in password:

            if character in guess_string:
                print(character)

            else:
                print("-")
                character_left += 1

        if character_left == 0:
            print(f"{user} WON!!!!!")
            break

        guess = input("Guess a word: ")
        guess_string += guess

        if guess not in password:
            live -= 1
            print("Nice try but not true ")
            print(f"{user} have {live} left")

            if live == 0:
                print(f"{user} Died!!!!!")
elif level_select == 2:
    live = 5
    password = f"{user}"
    print("İnfo: I think you are shine")
    while live > 0:
        character_left = 0
        for character in password:

            if character in guess_string:
                print(character)

            else:
                print("-")
                character_left += 1

        if character_left == 0:
            print(f"{user} WON!!!!!")
            break

        guess = input("Guess a word: ")
        guess_string += guess

        if guess not in password:
            live -= 1
            print("Nice try but not true ")
            print(f"{user} have {live} left")

            if live == 0:
                print(f"{user} Died!!!!!")

else:
    live = 15
    password = "Bulgaria"
    print("İnfo:The country, which declared its independence in 1908, witnessed World War I and the periods that followed.")
    while live > 0:
        character_left = 0
        for character in password:

            if character in guess_string:
                print(character)

            else:
                print("-")
                character_left += 1

        if character_left == 0:
            print(f"{user} WON!!!!!")
            break

        guess = input("Guess a word: ")
        guess_string += guess

        if guess not in password:
            live -= 1
            print("Nice try but not true ")
            print(f"{user} have {live} left")

            if live == 0:
                print(f"{user} Died!!!!!")



