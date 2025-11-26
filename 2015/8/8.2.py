from re import findall
with open("8.txt", "r", encoding="UTF-8") as f: lines = f.read().split("\n")

def main() -> int:
    score: int = 0
    for i in lines: 
        score += ((len(i) 
                    + 4
                    + 2 * len(findall(r'\\[\\"]', i)) 
                    + 1 * len(findall(r'(?=([^\\]|\\\\)\\x[0-9a-fA-F][0-9a-fA-F])', i))) 
                - len(i))
    return score

if __name__ == "__main__": print(main())