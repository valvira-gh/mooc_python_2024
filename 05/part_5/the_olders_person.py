

def add_a_person():
    people = []
    while True:
        name = input("Name:")
        year = int(input("Year:"))

        new_person = (name, year)
        people.append(new_person)
        
        selection = input("(N)ew person  || (Q)uit: ")

        if selection.lower() == "n":
            continue
        else:
            break
    
    return people


def oldest_person(people: list):
    for person in people:
        oldest_age = 0
        print(person)
        year = person[1]
        new_age = 2024 - year

        if new_age > oldest_age:
            oldest_age = new_age
            print('oa: ', oldest_age)
        

        print('age', oldest_age)


    return None


def main():
    people = add_a_person()
    print("People:", people)

    oldest = oldest_person(people)

    return None

main()