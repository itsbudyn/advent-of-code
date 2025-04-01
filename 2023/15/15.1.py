def main():
    with open("15.txt","r",encoding="UTF-8") as f: text = f.read().split(",")

    hash_sum = 0
    for i in text: 
        hash_value = 0
        for j in i:
            hash_value += ord(j)
            hash_value *= 17
            hash_value %= 256
        hash_sum += hash_value
    
    return hash_sum

if __name__ == "__main__": print(main())