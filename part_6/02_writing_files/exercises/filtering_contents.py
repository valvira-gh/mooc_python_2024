
def filter_contents_to_files():
    contents = {}
    
    # Alustetaan tiedostot tyhjentämällä ne
    with open("correct.csv", "w") as my_file:
        my_file.write("") # Tyhjennetään tiedosto

    with open("incorrect.csv", "w") as my_file:
        my_file.write("") # Tyhjennetään tiedosto

    # Luetaan CSV-tiedosto ja täytetään contents-sanakirja
    with open("exercises.csv") as new_file:
        for line in new_file:
            line = line.strip()
            parts = line.split(";")
            name = parts[0] # Oppilas
            exercise = parts[1] # Laskutehtävä
            answer = int(parts[2]) # Oppilaan vastaus

            # Lisätään oppilaan tiedot sanakirjaan, käytetään hyväksi listaa ja tuplea
            if name not in contents:
                contents[name] = []
            contents[name].append((exercise, answer))
    
    # Käydään contents-sanakirja läpi ja arvioidaan vastaukset
    for name, exercises in contents.items():
        for exercise, student_answer in exercises:
            # Puretaan laskutehtävä ja lasketaan oikea vastaus
            if '+' in exercise:
                num1, num2 = map(int, exercise.split('+'))
                correct_answer = num1 + num2
            elif '-' in exercise:
                num1, num2 = map(int, exercise.split('-'))
                correct_answer = num1 - num2
            else:
                continue

            # Luodaan rivi tiedostoon kirjoitettavaksi
            line = f"{name};{exercise};{student_answer}\n"
            if correct_answer == student_answer:
                with open("correct.csv", "a") as my_file:
                    my_file.write(line)
            else:
                with open("incorrect.csv", "a") as my_file:
                    my_file.write(line)
            
    print("Tehtävät jaettu oikeisiin ja vääriin vastauksiin!")
    return None


if __name__ == "__main__":
    filter_contents_to_files()

