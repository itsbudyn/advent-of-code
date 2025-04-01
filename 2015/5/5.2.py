def main():
    with open("5.txt","r",encoding="UTF-8") as f: text = f.readlines()

    nice = 0
    for i in text:
        pts = 0
        for j in range(len(i)-1):
            if i.count(i[j]+i[j+1]) >= 2:
                pts +=1
                break
            
        for j in range(1,len(i)-1):
            if i[j] != i[j-1] and i[j-1] == i[j+1]:
                pts +=1
                break

        if pts == 2: nice+=1
            
    return nice

if __name__ == "__main__": print(main())