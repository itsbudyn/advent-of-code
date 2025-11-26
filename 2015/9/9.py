from itertools import permutations

with open("2015/9/9.txt", "r", encoding="UTF-8") as f: lines = f.read().split("\n")

def main() -> tuple[int, int]:
    distances: dict[str, dict[str, int]] = {}
    for i in lines:
        line: list[str] = i.split(" ")
        for j in ((line[0], line[2], line[4]), (line[2], line[0], line[4])):
            target = {j[1]: int(j[2])}
            if j[0] in distances.keys(): distances[j[0]][j[1]] = int(j[2])
            else: distances[j[0]] = target
    
    routes: list[tuple[str, ...]] = list(permutations(list(distances.keys())))

    calculatedDistances: list[int] = []
    for route in routes:
        distance = 0
        for city in range(len(route) - 1): distance += distances[route[city]][route[city + 1]]
        calculatedDistances.append(distance)

    return min(calculatedDistances), max(calculatedDistances)

if __name__ == "__main__": print(main())