def create_tuple(x: int, y: int, z: int):
    if x < y and y < z:
        sorted_tuple = (x, z, y)
        return sorted_tuple
    
    


    return None

def main():
    tuple = create_tuple(1, 10, 3)
    print(tuple)



if __name__ == "__main__":
    main()

