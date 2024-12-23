from itertools import permutations

def main():
    with open("2024/23/23.txt","r",encoding="UTF-8") as f: text = f.read().split("\n")

    network = {}

    for connections in text: 
        connection = connections.split("-")
        if connection[0] not in network: network[connection[0]] = set([connection[1]])
        else: network[connection[0]].add(connection[1])
        if connection[1] not in network: network[connection[1]] = set([connection[0]])
        else: network[connection[1]].add(connection[0])

    threes = []

    for i in network.keys():
        for j in permutations(network[i], 2):
            if j[0] in network[j[1]]: 
                if set((i, j[0], j[1])) not in threes: threes.append(set((i, j[0], j[1])))

    p1 = 0
    for i in threes:
        i = tuple(i)
        if "t" in {i[0][0], i[1][0], i[2][0]}: p1 += 1
    

    sets = [threes[0]]
    goodSets = []
    for i in threes:
        three = list(i)
        setFound = False
        for j in range(len(sets)):
            if three[0] in sets[j] or three[1] in sets[j] or three[2] in sets[j]:
                sets[j] |= i
                setFound = True
                break
        if not setFound: sets.append(i)
        
    for i in sets: 
        interconnected = True
        for j in permutations(i, 2):
            if not (j[0] in network[j[1]] and j[1] in network[j[0]]):
                interconnected = False
                break
        if interconnected: goodSets.append(i)
    p2 = ",".join(i for i in (sorted(list(sorted(goodSets, key=len, reverse=True)[0]))))

    return f"Part 1: {p1}\nPart 2: {p2}"

if __name__ == "__main__": print(main())