def destination(used_map:list, source:int):
    for i in used_map[1:]:
        if source in range(i[1],i[1]+i[2]+1):
            return i[0] + source - i[1]
    return source

def main():
    with open("5.txt","r",encoding="UTF-8") as f: text = f.readlines()

    seeds = [int(i) for i in text[0][7:-1].split(" ")]

    map_arr = []
    for i in text[2:]:
        if "map" in i: map_arr.append([i])
        elif i != "\n": map_arr[-1].append([int(j) for j in i[:-1].split(" ")])

    for i in map_arr:
        for j in range(len(seeds)):
            seeds[j] = destination(i,seeds[j])

    return sorted(seeds)[0]

if __name__ == "__main__": print(main())