def main():
    with open("11.txt","r",encoding="UTF-8") as f: text = f.read().split(" ")
    stone_map = {}
    results = []

    for i in text:
        if i not in stone_map.keys(): stone_map[int(i)] = 1
        else: stone_map[int(i)] += 1
    
    for i in range(75):
        new_stone_map = {}
        for stone in list(stone_map.keys()):
            stoneStr = str(stone)
            newstones = []
            if stone == 0: newstones = (1,)
            elif not len(stoneStr) % 2: newstones = (int(stoneStr[len(stoneStr)//2:]), int(stoneStr[:len(stoneStr)//2]))
            else: newstones = (stone*2024,)

            for newstone in newstones:
                if newstone not in new_stone_map.keys(): new_stone_map[newstone] = stone_map[stone]
                else: new_stone_map[newstone] += stone_map[stone]
        stone_map = new_stone_map
        if i in {24, 74}: results.append(sum(stone_map.values()))

    return f"25 iterations (part 1): {results[0]}\n75 iterations (part 2): {results[1]}"

if __name__ == "__main__": print(main())