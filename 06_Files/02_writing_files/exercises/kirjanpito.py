import random
import string
from datetime import datetime
import time
# GLOBAALIT
kirjanpito = {} # Sanakirja tallentamaan tiedot paikallisesti
formatoitu_otsikkorivi = f"{'ID':<10}{'Asiakas':<15}{'Hevonen':<10}{'Määrä (kpl)':<12}{'Hinta (€)':<10}{'Loppusumma (€)':<15}{'Pvm':<10}{'Klo':<10}"

def luo_random_id() -> str:
    """Luo satunnaisen tunnisteen, joka sisältää kolme satunnaista kirjainta (A-G)
    ja kolme satunnaista numeroa."""
    kirjaimet = "".join(random.choices('ABCDEFG', k=3)) # Kolme satunnaista kirjainta väliltä A-G
    numerot = "".join(random.choices(string.digits, k=3)) # Kolme random numeroa väliltä 0-9
    random_id = kirjaimet + numerot
    return random_id

def tallenna_kirjanpito(tiedosto: str, kirjanpito: dict):
    """Kirjoittaa kirjanpidon tiedot paikallisesta sanakirjasta CSV-tiedostoon"""
    with open(tiedosto, "w") as my_file:
        my_file.write("id;asiakas;hevonen;määrä;taksa;loppuhinta;pvm;klo\n") # Otsikkorivi
        for id, tiedot in kirjanpito.items():
            rivi = f"{id};{';'.join(map(str, tiedot))}\n"
            my_file.write(rivi)

def tee_merkinta(tiedosto: str, id: str) -> dict:
    """Luo uuden merkinnän, kysyen käyttäjältä tarvittavat tiedot ja lisää merkinnän tiedostoon.
    Palauttaa merkinnän sanakirjaan."""
    while True:
        print("\n" + "############")
        print("TEE MERKINTÄ", end="\n" * 2)
        print("1 - Ratsastustunti, 2 - Ratsastus, 0 - Takaisin päävalikkoon")
        print()
        valinta = int(input("Valinta: "))

        if valinta == 1:
            while True:

                print("\n" + "############" +"\n")
               
                
                # Asiakastiedot ja hinnoittelu
                hevonen = input("Käytetty hevonen: ")
                asiakas = input("Asiakas: ")
                taksa = float(input("Hinta (euroa): "))
                maara = int(input("Määrä (kpl): "))
                loppuhinta = taksa * maara

                # Aikaleima
                now = datetime.now()
                pvm = now.strftime("%d-%m-%y")
                klo = now.strftime("%H:%M:%S")

                # Tulostetaan tiedot käyttäjälle tietojen validioimiseksi
                print()
                print("TARKISTA TIEDOT:")
                print(f"Pidetty ratsastustunti asiakas {asiakas.capitalize()} kanssa käyttäen hevosta {hevonen.capitalize()}.")
                print(f"Taksana ollut {taksa} euroa, mikä veloitettu {maara} asiakkaalta. ")
                print(f"Täten veloitettu yhteensä {loppuhinta} euroa.")
                print()
                
                # Vahvistus
                print("Vahivstetaanko valinta? (k/e)")
                vahvistus = input("Valinta: ")
                if vahvistus.lower() == 'k':
                    # Luodaan satunnainen id ja muutetaan tiedot csv-tiedostoon sopivaan muotoon
                    id = luo_random_id()
                    rivi = f"{id};{asiakas};{hevonen};{maara};{taksa};{loppuhinta};{pvm};{klo}\n"
                    # Lisätään tiedot tiedostoon uudelle riville
                    with open("kirjanpito.csv", "a") as my_file:
                        my_file.write(rivi)
                        print()
                        print(f"Merkintä (ID: {id}) tallennettu tiedostoon: {tiedosto}")
                        kirjanpito[id] = [asiakas, hevonen, maara, taksa, loppuhinta, pvm, klo]  # Päivitä sanakirjaan
                        time.sleep(2)
                        return kirjanpito
                else:
                    print("Merkintää ei tallennettu.")
                    time.sleep(2)
                    return kirjanpito  
        elif valinta == -1 or valinta == 0:
            break


def lue_kirjanpito(tiedosto: str) -> dict:
    """Lataa kirjanpidon tiedot tiedostosta sanakirjaan ja palauttaa sanakirjan."""
    merkinnat = {}  # Paikallinen sanakirja tiedoille
    try:
        with open(tiedosto, "r") as my_file:
            for rivi in my_file:
                rivi = rivi.strip()
                osa = rivi.split(";")
                if osa[0] == "id":
                    continue  # Ohitetaan otsikkorivi
                merkinnat[osa[0]] = osa[1:]
        return merkinnat
    except FileNotFoundError:
        print("Virhe: Tiedostoa ei löydy. Tarkista tiedoston nimi ja polku.")
        return merkinnat  # Palautetaan tyhjä sanakirja virhetilanteessa

def tulosta_kirjanpito(kirjanpito: dict):
    """Tulostaa kirjanpidon tasaisesti muotoiltuna taulukkona."""
    print("\n" + "#############" + "\n")

    print("KIRJANPIDON NÄKYMÄ", end="\n" * 3)
    
    # Tulostetaan otsikot
    print(formatoitu_otsikkorivi)
    print("-" * 80)
    
    # Tulostetaan tiedot rivi riviltä
    for id, tiedot in kirjanpito.items():
        # Tarkistetaan, että rivillä on riittävästi tietoja tulostettavaksi
        if len(tiedot) == 7: 

            print(f"{id:<10}{tiedot[0]:<15}{tiedot[1]:<10}{tiedot[2]:<12}{tiedot[3]:<10}{tiedot[4]:<15}{tiedot[5]:<10}{tiedot[6]:<10}")
        else:
            print(f"Riviä {id} ei voi tulostaa: puuttuvia tietoja.")
    
    print()
    print("TOIMINNOT: 1 - Rajaa näkymää, 2 - Muokkaa merkintää, 0 - Palaa päävalikkoon")
    toiminto = int(input("Toiminto: "))

    if toiminto == 1:
        
        pass
    elif toiminto == 2:
        print()
        kohde_id = input("Anna muokattavan merkinnän ID-tunniste: ")
        if len(kohde_id) != 6:
            print("Virheellinen ID, anna kuusi merkkiä pitkä id.")
        else:
            muokkaa_merkintaa(kohde_id)

        
    return None

def muokkaa_merkintaa(kohde_id: str):
    """Muokkaa olemassa olevaa merkintää ja päivittää sekä sanakirjan että tiedoston"""
    kirjanpito = lue_kirjanpito("kirjanpito.csv")  # Lataa kirjanpito sanakirjaan

    if kohde_id not in kirjanpito:
        print("Virhe: ID ei ole olemassa.")
        return

    # Tulostetaan valitun merkinnän tiedot
    tiedot = kirjanpito[kohde_id]
    print(f"\nAsiakas: {tiedot[0]}, Hevonen: {tiedot[1]}, Määrä: {tiedot[2]}, Hinta: {tiedot[3]}, Loppusumma: {tiedot[4]}, Pvm: {tiedot[5]}, Klo: {tiedot[6]}\n")

    # Muokkausvaihtoehdot
    print("Mitä kohtaa haluat muokata?\n1 - Asiakas, 2 - Hevonen, 3 - Määrä, 4 - Hinta, 0 - Palaa edelliseen")
    toiminto = int(input("Valinta: "))

    if toiminto == 1:
        tiedot[0] = input("Uusi arvo kohtaan asiakas: ")
    elif toiminto == 2:
        tiedot[1] = input("Uusi arvo kohtaan hevonen: ")
    elif toiminto == 3:
        tiedot[2] = input("Uusi arvo kohtaan määrä: ")
    elif toiminto == 4:
        tiedot[3] = input("Uusi arvo kohtaan hinta: ")
        tiedot[4] = str(float(tiedot[2]) * float(tiedot[3]))  # Päivitetään loppusumma
    elif toiminto == 0:
        return

    kirjanpito[kohde_id] = tiedot  # Päivitä sanakirjaan
    
    # Päivitetään koko kirjanpito CSV-tiedostoon
    with open("kirjanpito.csv", "w") as my_file:
        my_file.write("id;asiakas;hevonen;määrä;taksa;loppuhinta;pvm;klo\n")  # Otsikkorivi
        for id, tiedot in kirjanpito.items():
            rivi = f"{id};" + ";".join(tiedot) + "\n"
            my_file.write(rivi)
    print("Merkintä päivitetty.\n")


def main():
    global kirjanpito
    # kirjanpito = {} # Alustetaan sanakirja kerran, jotta vältetään myöhemmät ongelmat
    # Pääsilmukka
    while True:
        print("\n" * 3)
        print("*** KIRJANPITOSOVELLUS ***")
        print("PÄÄVALIKKO", end="\n" * 2)
        print("1 - Tee uusi merkintä, 2 - Avaa kirjanpito, 0 - Lopeta")
        valinta = int(input("Valinta: "))

        if valinta == 1:
           random_id = luo_random_id()
           kirjanpito[id] = tee_merkinta("kirjanpito.csv", random_id)
        elif valinta == 2:
            kirjanpito = lue_kirjanpito("kirjanpito.csv")
            tulosta_kirjanpito(kirjanpito)
        elif valinta == -1 or valinta == 0:
            break
    
    return None

if __name__ == "__main__":
    print("\tPuppe Tech")
    print("\t 2024 (c)")
    time.sleep(0.5)

    main()
    # Testauksessa käytettävä tiedoston alustus
    # with open("kirjanpito.csv", "w") as my_file:
    #     my_file.write("id;asiakas;hevonen;määrä;taksa;loppuhinta;pvm;klo\n")

    