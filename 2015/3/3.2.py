def main():
    with open("3.txt","r",encoding="UTf-8") as f: text = f.read()

    coords_santa = [[0,0]]
    coords_robot = [[0,0]]
    newcoord_santa = [0,0]
    newcoord_robot = [0,0]

    for i in range(len(text)):    
        match i%2:
            case 0: newcoord = newcoord_santa.copy()
            case 1: newcoord = newcoord_robot.copy()

        match text[i]:
            case ">": newcoord[1]+=1
            case "v": newcoord[0]+=1
            case "<": newcoord[1]-=1
            case "^": newcoord[0]-=1

        match i%2:
            case 0:
                if newcoord not in coords_santa: coords_santa.append(newcoord.copy())
                newcoord_santa = newcoord.copy()
            case 1:
                if newcoord not in coords_santa: coords_robot.append(newcoord.copy())
                newcoord_robot = newcoord.copy()

    houses = coords_santa.copy()
    for i in coords_robot:
        if i not in houses: houses.append(i)

    return len(houses)

if __name__ == "__main__": print(main())