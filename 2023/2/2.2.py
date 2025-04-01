import re

def main():
    with open("2.txt","r") as f: text = f.read()
    games = text.split("\n")

    powers_sum = 0

    for i in range(len(games)):
        games[i] = games[i].split(" ")[1::]
        games[i][0] = int(games[i][0][:-1])
        for j in range(1, len(games[i])):
            if re.match(r".*[0-9].*",games[i][j]): games[i][j] = int(games[i][j])
            elif games[i][j][-1] in ";,": games[i][j] = games[i][j][:-1]

    for i in range(len(games)):
        reds, grns, blus = 0,0,0

        for j in range(len(games[i])):
            match games[i][j]:
                case "red": 
                    if games[i][j-1] > reds: reds=games[i][j-1]
                case "green":
                    if games[i][j-1] > grns: grns=games[i][j-1]
                case "blue":
                    if games[i][j-1] > blus: blus=games[i][j-1]

        powers_sum+=reds*grns*blus
    return powers_sum

if __name__ == "__main__": print(main())