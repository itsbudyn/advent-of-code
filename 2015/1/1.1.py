def main(): 
    with open("1.txt","r",encoding="UTF-8") as f: text = f.read()
    return text.count("(") - text.count(")")
    
if __name__ == "__main__": print(main())