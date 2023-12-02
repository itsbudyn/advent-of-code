import re

def main():
    with open("2.txt","r") as f: text = f.read()
    games = text.split("\n")

    allowed_reds = 12
    allowed_grns = 13
    allowed_blus = 14

    gids_sum = 0

    for i in range(len(games)):
        games[i] = games[i].split(" ")[1::]
        games[i][0] = int(games[i][0][:-1])
        for j in range(1, len(games[i])):
            if re.match(r".*[0-9].*",games[i][j]): games[i][j] = int(games[i][j])

    for i in range(len(games)):
        reds, grns, blus = 0,0,0
        valid = True

        for j in range(len(games[i])):
            match games[i][j]:
                case "red"|"red,"|"red;": reds+=games[i][j-1]
                case "green"|"green,"|"green;": grns+=games[i][j-1]
                case "blue"|"blue,"|"blue;": blus+=games[i][j-1]
        
            if reds > allowed_reds or grns > allowed_grns or blus > allowed_blus: 
                valid = False
                break
            if ";" in str(games[i][j]): reds, grns, blus = 0, 0, 0
        if valid: gids_sum+=games[i][0]

    return gids_sum

if __name__ == "__main__": print(main())