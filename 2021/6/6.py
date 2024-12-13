def main():
    with open("2021/6/6.txt","r",encoding="UTF-8") as f: text = f.read()
    results = []
    lanternfish = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for i in text.split(","): lanternfish[int(i)]+=1
    for i in range(256):
        lanternfish_old = lanternfish.copy()
        for j in range(1,9):
            lanternfish[j-1] = lanternfish[j]
            lanternfish[j] = 0
        lanternfish[6] += lanternfish_old[0]
        lanternfish[8] += lanternfish_old[0]

        if i in [79,255]: results.append(sum(lanternfish.values()))
    return f"Part 1:{results[0]}\nPart 2:{results[1]}"

if __name__ == "__main__": print(main())