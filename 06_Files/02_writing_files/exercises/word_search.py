


def find_words(search_term: str) -> list:
    word_list = []

    

    
    with open("words.txt") as my_file:
        for line in my_file:
            words = line.strip().split(", ")
            # print('words:', words)

            for word in words:
                if search_term.startswith("*"):
                    if word.endswith(search_term[1:]):
                        word_list.append(word)

                
                

    return word_list


if __name__ == "__main__":
    while True:
        search_term = input("Search term: ")
        if search_term == "0":
            break
        else:
            results = find_words(search_term)
            break
    print(results)