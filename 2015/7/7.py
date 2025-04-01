from functools import lru_cache
import re

def getWire(wire:str):
    for i in text:
        if i[1] == wire: return i[0]

@lru_cache(maxsize=None)
def getSignal(wire:str):
    mapped = False
    while not mapped:
        mapped = True
        wire = wire.split(" ")
        for i in range(len(wire)):
            if re.search(r"[a-z]+",wire[i]):
                mapped = False
                wire[i] = getSignal(getWire(wire[i]))
        if type(wire) == list: wire = " ".join(wire)

    return str(eval(wire))

def main():
    results = []
    lut = {
            "AND"     : "&",
            "OR"      : "|",
            "XOR"     : "^",
            "NOT"     : "~",
            "LSHIFT"  : "<<",
            "RSHIFT"  : ">>"
        }
    for part in range(2):
        with open("2015/7/7.txt","r",encoding="UTF-8") as f: 
            global text
            text = f.read()
            if results: text = re.sub(r"^b | b$", " "+results[0]+" ", text, flags=(re.M))
            text = text.splitlines()

        for i in range(len(text)): 
            for j in lut:
                if j in text[i]:
                    text[i]=text[i].replace(j,lut[j])
                    break
            text[i]=text[i].split(" -> ")

        results.append(getSignal(getWire("a")))
        getSignal.cache_clear()
    return f"Part 1:{results[0]}\nPart2:{results[1]}"

if __name__ == "__main__": print(main())