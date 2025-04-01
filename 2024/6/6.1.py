def main():
    with open("6.txt","r",encoding="UTF-8") as f: text = f.read().split("\n")
    nextpos = []
    tail = []
    distinctPositions = 1
    bearing = 0

    text = list(map(list, text))

    for y in range(len(text)):
        if len(nextpos): break
        for x in range(len(text[0])):
            if text[y][x] == "^": 
                nextpos = [x, y-1]
                break
    tail.append(nextpos.copy())

    while True:
        for i in nextpos:
            if i >= len(text) or 0 > i: return distinctPositions
        match text[nextpos[1]][nextpos[0]]:
            case ".":
                distinctPositions += 1
                text[nextpos[1]][nextpos[0]] = "X"
            case "#": 
                bearing += 90
                bearing %= 360
                nextpos = tail[0].copy()

        match bearing:
            case 0:     nextpos = [nextpos[0],nextpos[1]-1]
            case 90:    nextpos = [nextpos[0]+1,nextpos[1]]
            case 180:   nextpos = [nextpos[0],nextpos[1]+1]
            case 270:   nextpos = [nextpos[0]-1,nextpos[1]]
        
        tail.append(nextpos.copy())
        if len(tail) > 2: tail.pop(0)

if __name__ == "__main__": print(main())