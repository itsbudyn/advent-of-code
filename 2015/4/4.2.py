from hashlib import md5

def main():
    with open("2015/4/4.txt","r",encoding="UTF-8") as f: text = f.read()

    i = 0
    while True:
        if md5((text+str(i)).encode()).hexdigest()[:6] == "000000": return i
        else: i+=1

if __name__ == "__main__": print(main())