



if __name__ == "__main__":
    print("*** ACCOUNTER ***")
    print()

    while True:
        print("#####\n")
        user_input = int(input("1 - New action, 2 - Read actions, 0 - Quit: "))
        print("\n#####\n")

        if user_input == 1:
            while True:
                print("In which animal is action about?")
                animal = int(input("1 - Horses, 2 - Sheeps, 3 - Chickens, 4 - Dogs, 0 - Previous screen: "))
                if animal == 1:
                    print("Action type?")
                    action_type = int(input("1 - Giving a lesson, 2 - Riding a horse, 0 - Previous screen: "))

                    if action_type == 1:
                        pass
                    elif action_type == 2:
                        pass
                    elif action_type == -1 or 0:
                        break
                elif animal == 2:
                    pass
                elif animal == 3:
                    pass
                elif animal == 4:
                    pass
                elif animal == 0 or -1:
                    break

        elif user_input == 2:
            pass
        elif user_input == 0:
            break
