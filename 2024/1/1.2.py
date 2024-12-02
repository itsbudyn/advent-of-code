def main():
    with open("1.txt","r",encoding="UTF-8") as f: text = f.readlines()

    arrs = [{},{}]

    for i in text:
        line = i.split("  ")
        n1, n2 = int(line[0]), int(line[1])
        
        if n1 in arrs[0].keys():
            arrs[0][n1] += 1
        else: arrs[0][n1] = 1

        if n2 in arrs[1].keys():
            arrs[1][n2] += 1
        else: arrs[1][n2] = 1

    distsim = 0

    for i in arrs[0].keys():
        if i in arrs[1].keys(): distsim += i*arrs[1][i]*arrs[0][i]

    return distsim

if __name__ == "__main__": print(main())