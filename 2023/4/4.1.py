import re

def main():
    with open("4.txt","r",encoding="UTF-8") as f: text = f.readlines()

    games = []
    total_pts = 0

    for i in range(len(text)):
        text[i] = text[i].split(":")[1].split("|")
        game = []
        for j in text[i]: game.append(re.findall(r"[0-9]+",j))
        games.append(game)

    for i in games:
        pts = 0
        for j in i[1]:
            if j in i[0]: 
                if pts == 0: pts+=1
                else: pts *=2
        total_pts += pts

    return total_pts

if __name__ == "__main__": print(main())