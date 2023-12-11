def expand(galaxy_map:list):
    for i in range(len(galaxy_map)): galaxy_map[i] = list(galaxy_map[i])

    for i in range(len(galaxy_map)):
        if not galaxy_map[i].count("#"): 
            for j in range(len(galaxy_map[i])): galaxy_map[i][j] = "M"

    for i in range(len(galaxy_map[0])):
        emptyColumn = True
        for j in range(len(galaxy_map)):
            if galaxy_map[j][i] not in ".M": 
                emptyColumn = False
                break
        if emptyColumn:
            for j in range(len(galaxy_map)): galaxy_map[j][i] = "M"

    return galaxy_map

def getGalaxyPairs(galaxy_map:list):
    galaxies = []
    galaxy_pairs = []

    for i in range(len(galaxy_map)): 
        for j in range(len(galaxy_map[i])):
            if galaxy_map[i][j] == "#": galaxies.append([i,j])

    for i in range(len(galaxies)):
        for j in range(i+1,len(galaxies)):
            galaxy_pairs.append([galaxies[i],galaxies[j]])

    return galaxy_pairs

def getShortestPath(galaxy_map:list, galaxy_pair:list):
    jump = 1000000
    x_steps = 0
    y_steps = 0

    if galaxy_pair[1][1] < galaxy_pair[0][1]: x_range = range(galaxy_pair[1][1],galaxy_pair[0][1])
    else: x_range = range(galaxy_pair[0][1],galaxy_pair[1][1])

    if galaxy_pair[1][0] < galaxy_pair[0][0]: y_range = range(galaxy_pair[1][0],galaxy_pair[0][0])
    else: y_range = range(galaxy_pair[0][0],galaxy_pair[1][0])

    for i in x_range:
        if galaxy_map[galaxy_pair[1][0]][i] == "M": x_steps += jump
        else: x_steps += 1

    for i in y_range:      
        if galaxy_map[i][galaxy_pair[1][1]] == "M": y_steps += jump
        else: y_steps += 1
    
    return x_steps + y_steps 

def main():
    with open("11.txt","r",encoding="UTF-8") as f: text=f.read().splitlines()
    
    text = expand(text)
    galaxy_pairs = getGalaxyPairs(text)

    paths_sum = 0
    for i in range(len(galaxy_pairs)): paths_sum += getShortestPath(text, galaxy_pairs[i])

    return paths_sum

if __name__ == "__main__": print(main())