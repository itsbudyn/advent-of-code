with open("2015/1/1.txt","r",encoding="UTF-8") as f: text = f.read()

def main(): return text.count("(") - text.count(")")
    
if __name__ == "__main__": print(main())