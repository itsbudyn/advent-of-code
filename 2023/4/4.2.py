import re

def hits(game):
    score = 0
    for i in game[0]:
        if i in game[1]: score += 1
    return score

def main():
    with open("4.txt","r",encoding="UTF-8") as f: text = f.readlines()

    games = []
    points_games = []  
    
    for i in range(len(text)):
        text[i] = text[i].split(":")[1].split("|")
        game = []
        for j in text[i]: game.append(re.findall(r"[0-9]+",j))
        games.append(game)

    to_check = list(range(0,len(games)))

    for i in games: points_games.append(hits(i))

    i = 0
    while i < len(to_check):
        newcards = list(range(to_check[i]+1,to_check[i]+points_games[to_check[i]]+1))
        for j in newcards[::-1]:
            to_check.insert(i+1,j)
        i+=1

    return len(to_check)        

if __name__ == "__main__": print(main())