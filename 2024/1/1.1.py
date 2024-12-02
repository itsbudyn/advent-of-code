def main():
    with open("1.txt","r",encoding="UTF-8") as f: text = f.readlines()

    arrs = [[],[]]

    for i in text:
        line = i.split("  ")
        arrs[0].append(int(line[0]))
        arrs[1].append(int(line[1]))

    arrs[0], arrs[1] = sorted(arrs[0]), sorted(arrs[1])
    
    distsum = 0
    for i in range(len(arrs[0])):
        distsum += abs(arrs[0][i] - arrs[1][i])

    return distsum

if __name__ == "__main__": print(main())