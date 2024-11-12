# Apufunktio, joka lukee tiedoston ja palauttaa matriisin listojen listana
def read_matrix():
    matrix = []
    with open("matrix.txt") as file:
        for line in file:
            # Poistetaan rivinvaihdot ja muut ylimääräiset merkit lopusta, jaetaan pilkulla
            row = list(map(int, line.strip().split(",")))  # Muunnetaan rivin merkkijonot int:ksi
            matrix.append(row)  # Lisätään rivi matriisiin
    return matrix

def matrix_max():
    matrix = read_matrix() # Apufunktio lukee
    highest_num = 0
    for row in matrix:
        for item in row:
            if item > highest_num:
                highest_num = item
    
    return highest_num

def row_sums():
    matrix = read_matrix()
    sums = []
    for row in matrix:
        sum = 0
        for num in row:
            sum += num
        sums.append(sum)
    
    return sums


def matrix_sum():
    matrix = read_matrix() # Apufunktio lukee
    total_sum = 0
    for row in matrix:
        total_sum += sum(row) # Lasketaan rivien summa ja lisätään kokonaissummaan
    
    return total_sum

if __name__ == "__main__":
    matrix = read_matrix()
    sum = matrix_sum()
    max = matrix_max()
    sums = row_sums()
    print('sum:', sum)
    print('max:', max)
    print('row sums:', sums)





