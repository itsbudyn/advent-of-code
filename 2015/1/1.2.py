def main(): 
    with open("1.txt","r",encoding="UTF-8") as f: text = f.read()
    floor = 0
    for i in range(len(text)):
        match text[i]:
            case "(": floor+=1
            case ")": floor-=1
        if floor == -1: return i+1
    
if __name__ == "__main__": print(main())