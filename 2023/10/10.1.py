def getAvailablePaths(arr:list, pos:list):
    available = []

    available_directions = ""
    match arr[pos[1]][pos[0]]:
        case "|": available_directions += "NS"
        case "-": available_directions += "EW"
        case "L": available_directions += "NE"
        case "J": available_directions += "NW"
        case "7": available_directions += "SW"
        case "F": available_directions += "SE"
        case "S": available_directions += "NEWS"
        
    if pos[1] != 0 and "N" in available_directions and arr[pos[1]-1][pos[0]] in "|7FS": available.append([pos[0],pos[1]-1])
    if pos[1] != len(arr)-1 and "S" in available_directions and arr[pos[1]+1][pos[0]] in "|JLS": available.append([pos[0],pos[1]+1])
    if pos[0] != 0 and "W" in available_directions and arr[pos[1]][pos[0]-1] in "-FLS": available.append([pos[0]-1,pos[1]])
    if pos[0] != len(arr[0])-1 and "E" in available_directions and arr[pos[1]][pos[0]+1] in "-J7S": available.append([pos[0]+1,pos[1]])

    return available

def main():
    with open("10.txt","r",encoding="UTF-8") as f: text = f.read().splitlines()

    start = []

    for i in range(len(text)):
        for j in range(len(text[0])): 
            if text[i][j] == "S": 
                start = [j,i]
                break
        if start: break

    paths = [[start]]
    loops = []

    while paths:
        newpaths = []

        for i in paths:
            available_nodes = getAvailablePaths(text,i[-1])

            for j in available_nodes:
                newpath = i.copy()

                newpath.append(j)
                if j not in i: newpaths.append(newpath)
                elif j == start: loops.append(newpath)
            
        paths = newpaths.copy()

    return len(loops[-1])//2

if __name__ == "__main__": print(main())