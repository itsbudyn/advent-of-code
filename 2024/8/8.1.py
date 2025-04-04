def main():
    with open("8.txt","r",encoding="UTF-8") as f: text = f.read().split("\n")

    text = list(map(list, text))
    antennas = {}
    antinodes = set()

    for y in range(len(text)):
        for x in range(len(text[y])):
            if text[y][x] != ".":
                if text[y][x] not in antennas.keys(): antennas[text[y][x]] = [(x,y)]
                else: antennas[text[y][x]].append((x,y))

    for ant in antennas.keys():
        for coord1 in range(len(antennas[ant])-1):
            for coord2 in range(coord1+1, len(antennas[ant])):
                coordDistance = [abs(antennas[ant][coord1][0] - antennas[ant][coord2][0]), abs(antennas[ant][coord1][1] - antennas[ant][coord2][1])]
                if antennas[ant][coord1][0] > antennas[ant][coord2][0]: coordDistance[0]*=-1
                if antennas[ant][coord1][1] > antennas[ant][coord2][1]: coordDistance[1]*=-1
                newAntinodes = (
                    (antennas[ant][coord1][0] - coordDistance[0], antennas[ant][coord1][1] - coordDistance[1]),
                    (antennas[ant][coord2][0] + coordDistance[0], antennas[ant][coord2][1] + coordDistance[1])
                )
                for newAntinode in newAntinodes:
                    if min(newAntinode[0], newAntinode[1]) >= 0 and max(newAntinode[0], newAntinode[1]) < len(text): antinodes.add(newAntinode)

    return len(antinodes)

if __name__ == "__main__": print(main())