def main():
    with open("14.txt","r",encoding="UTF-8") as f: text = f.read().splitlines()

    for i in range(len(text)): text[i] = list(text[i])

    for i in range(1,len(text)):
        for j in range(len(text[i])):
            if text[i][j] == "O":
                new_y = i
                for k in range(i-1,-1,-1):
                    if text[k][j] == ".": new_y = k
                    else: break
                text[i][j] = "."
                text[new_y][j] = "O"

    load = 0
    for i in range(len(text)): load += text[i].count("O") * (len(text)-i)

    return load

if __name__ == "__main__": print(main())