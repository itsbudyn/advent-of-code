def expand(galaxy_map:list):
    for i in range(len(galaxy_map)): galaxy_map[i] = list(galaxy_map[i])

    recentlyExpanded = False
    for i in range(len(galaxy_map)):
        if not recentlyExpanded and not galaxy_map[i].count("#"): 
            galaxy_map.insert(i,galaxy_map[i].copy())
            recentlyExpanded = True
        elif recentlyExpanded: recentlyExpanded = False

    recentlyExpanded = False
    i = 0
    while i < len(galaxy_map[0]):
        emptyColumn = True
        if recentlyExpanded: recentlyExpanded = False
        else:
            for j in range(len(galaxy_map)):
                if galaxy_map[j][i] != ".": 
                    emptyColumn = False
                    break
            if emptyColumn:
                for j in range(len(galaxy_map)): 
                    galaxy_map[j].insert(i,".")
                recentlyExpanded = True
        i+=1

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

def getShortestPath(galaxy_pair:list):
    length = abs(galaxy_pair[1][1] - galaxy_pair[0][1])
    width = abs(galaxy_pair[1][0] - galaxy_pair[0][0])
    return length + width

def main():
    with open("11.txt","r",encoding="UTF-8") as f: text=f.read().splitlines()
    
    text = expand(text)
    galaxy_pairs = getGalaxyPairs(text)

    paths_sum = 0
    for i in range(len(galaxy_pairs)): paths_sum += getShortestPath(galaxy_pairs[i])

    return paths_sum

if __name__ == "__main__": print(main())