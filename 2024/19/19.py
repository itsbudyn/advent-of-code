from functools import lru_cache

@lru_cache
def getCombos(towel:str, patterns:tuple):
    combos = 0
    for pattern in patterns:
        if towel.startswith(pattern):
            if len(towel) == len(pattern): combos += 1
            else: combos += getCombos(towel[len(pattern):], patterns)
    return combos

def main():
    with open("2024/19/19.txt","r",encoding="UTF-8") as f: text = f.read().split("\n\n")
    patterns = tuple(text[0].split(", "))
    designs = text[1].split("\n")
    
    results = [0, 0]
    for design in designs:
        combos = getCombos(design, patterns)
        results[0] += combos != 0
        results[1] += combos

    return f"Part 1: {results[0]}\nPart 2: {results[1]}"

if __name__ == "__main__": print(main())