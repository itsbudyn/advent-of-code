def main():
    with open("2024/25/25.txt","r",encoding="UTF-8") as f: schematics = f.read().split("\n\n")

    locks = set()
    keys = set()

    for i in schematics: 
        schema = list(zip(*map(list, i.split("\n"))))
        heights = [0, 0, 0, 0, 0]
        for j in range(len(schema)): heights[j] = schema[j].count("#")-1
        if set(i[0]) == {"#"}: locks.add(tuple(heights))
        else: keys.add(tuple(heights))

    fits = 0
    for lock in locks:
        for key in keys:
            fit = True
            for i in range(5):
                if lock[i] + key[i] >= 6:
                    fit = False
                    break
            if fit: fits+=1
    return fits 

if __name__ == "__main__": print(main())