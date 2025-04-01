def main():    
    with open("4.txt","r",encoding="UTF-8") as f: text = f.read().split("\n")

    matches = 0

    for y in range(1,len(text)-1):
        for x in range(1,len(text[0])-1):
            if text[y][x] == "A": 
                if {text[y-1][x-1], text[y+1][x+1]} == {text[y-1][x+1], text[y+1][x-1]} == {"S","M"}: matches+=1

    return matches

if __name__ == "__main__": print(main())