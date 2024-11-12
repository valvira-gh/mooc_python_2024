# completed

def read_input(input_text: str, min_num: int, max_num: int) -> int:
    while True:
        
        try:
            number = int(input(input_text))

            if number >= min_num and number <= max_num:
                return number
            else:
                print(f"You must type in an integer between {min_num} and {max_num}")
        except ValueError:
            print(f"You must type in an integer between {min_num} and {max_num}")
            

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in: ", number)