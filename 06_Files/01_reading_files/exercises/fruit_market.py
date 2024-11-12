
def read_fruits(file: str):
    # Alustetaan tyhjä sanakirja
    contents = {}

    # Avataan csv-tiedosto
    with open(file) as new_file:
        # Luetaan se rivi riviltä
        for line in new_file:
            # Poistetaan turha rivinvaihtomerkki lopusta
            line = line.rstrip()
            # Jaetaan rivi kahteen osaan separaattori-merkistä
            parts = line.split(";")
            # Tallennetaan sanakirjaan loopin sisällä käyttäen avaimena 1. arvoa
            # Ja arvona float-tyyppistä hinta-numeroa.
            contents[parts[0]] = float(parts[1])
            
    return contents



if __name__ == "__main__":
    contents = read_fruits("fruits.csv")



