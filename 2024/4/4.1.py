def main():    
    with open("4.txt","r",encoding="UTF-8") as f: text = f.read().split("\n")

    matches = 0
    dimensions = (len(text[0]),len(text))

    for y in range(len(text)):
        for x in range(len(text[0])):
            if text[y][x] == "X":
                eastSpace = dimensions[0] - x >= 4
                westSpace = x >= 3
                northSpace = y >= 3
                southSpace = dimensions[1] - y >= 4
                word = ""

                # E
                if eastSpace:
                    for i in range(x, x+4): word+=text[y][i]
                    if word == "XMAS": matches+=1
                    word=""
                # W
                if westSpace:
                    for i in range(x, x-4, -1): word+=text[y][i]
                    if word == "XMAS": matches+=1
                    word=""
                # N
                if northSpace:
                    for i in range(y, y-4, -1): word+=text[i][x]
                    if word == "XMAS": matches+=1
                    word=""
                # S
                if southSpace:
                    for i in range(y, y+4): word+=text[i][x]
                    if word == "XMAS": matches+=1
                    word=""
                # NE
                if northSpace and eastSpace:
                    for i in range(4): word+=text[y-i][x+i]
                    if word == "XMAS": matches+=1
                    word=""
                # SE
                if southSpace and eastSpace:
                    for i in range(4): word+=text[y+i][x+i]
                    if word == "XMAS": matches+=1
                    word=""
                # SW
                if southSpace and westSpace:
                    for i in range(4): word+=text[y+i][x-i]
                    if word == "XMAS": matches+=1
                    word=""
                # NW
                if northSpace and westSpace:
                    for i in range(4): word+=text[y-i][x-i]
                    if word == "XMAS": matches+=1
                    word=""

    return matches

if __name__ == "__main__": print(main())