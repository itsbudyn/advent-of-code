def main():
    with open("3.txt","r",encoding="UTf-8") as f: text = f.read()

    coords = [[0,0]]
    newcoord = coords[0].copy()

    for i in text:    
        match i:
            case ">": newcoord[1]+=1
            case "v": newcoord[0]+=1
            case "<": newcoord[1]-=1
            case "^": newcoord[0]-=1
        if newcoord not in coords: coords.append(newcoord.copy())
    return len(coords)

if __name__ == "__main__": print(main())