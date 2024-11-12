
def store_personal_data(person: tuple) -> None:
    name = str(person[0])
    age = int(person[1])
    height = float(person[2])
    line = f"{name};{age}; {height}\n"


    with open("people.csv", "a") as my_file:
        my_file.write(line)

    return None


if __name__ == "__main__":
    store_personal_data(("Paul Paulson", 37, 178.5))
    store_personal_data(("Valtteri Virtanen", 33, 185.0))