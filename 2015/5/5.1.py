import re

def main():
    with open("5.txt","r",encoding="UTF-8") as f: text = f.readlines()

    nice = 0
    for i in text:
        if re.findall(r"(.*[aeiou]){3,}",i) and re.findall(r"(\w)\1+",i) and not re.findall(r"(ab|cd|pq|xy)+",i): nice+=1
            
    return nice

if __name__ == "__main__": print(main())