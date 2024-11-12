

while True:
    with open("dictionary.txt") as new_file:
        for line in new_file:
            line = line.strip()

          


    user_input = int(input("1 - Add word, 2 - Search, 3 - Quit: "))

    if user_input == 1:
        finnish_word = input("The word in Finnish: ")
        english_word = input("The word in English: ")
        line = f"{finnish_word};{english_word}\n"

        with open("dictionary.txt", "a") as my_file:
            my_file.write(line)
    
    elif user_input == 2:
        search_term = input("Search term: ")
        
        with open("dictionary.txt") as my_file:
            for line in my_file:
                line = line.strip()
                words = line.split(";")
                

                if search_term in words:
                    print(f"{words[0]} - {words[1]}")
                    


    elif user_input == 3:
        break
        
