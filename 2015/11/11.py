def main() -> list[str]:
    def incrementPassword(password: str) -> str:
        passwordList:list[str] = list(password)

        for offset in range(len(passwordList)):
            if ord(passwordList[-1 - offset]) == 122: passwordList[-1 - offset] = "a"
            else:
                passwordList[-1 - offset] = chr(ord(passwordList[-1 - offset]) + 1)
                return "".join(passwordList)
        return ""

    def charCompliance(checkedStr: str) -> bool: return not any(bannedChar in checkedStr for bannedChar in ("i", "o", "l"))

    straights: list[str] = []
    seq: list[str] = ["a", "b", "c"]
    for _ in range(24):
        newseq = "".join(seq)
        if charCompliance(newseq): straights.append(newseq)
        for j in range(3):
            seq[j] = chr(ord(seq[j]) + 1)
    def straightCompliance(checkedStr: str, straights: list[str]) -> bool: return any(straight in checkedStr for straight in straights)

    pairs: list[str] = []
    seq: list[str] = ["a", "a"]
    for _ in range(26):
        newseq = "".join(seq)
        if charCompliance(newseq): pairs.append(newseq)
        for j in range(2):
            seq[j] = chr(ord(seq[j]) + 1)
    def pairCompliance(checkedStr: str, pairs: list[str]) -> bool:
        count = 0
        for pair in pairs:
            if pair in checkedStr: count += 1
            if count >= 2: return True
        return False

    def passwordCompliance(checkedStr: str) -> bool: return charCompliance(checkedStr) and straightCompliance(checkedStr, straights) and pairCompliance(checkedStr, pairs)
    
    with open("11.txt", "r", encoding="UTF-8") as f: pwd: str = f.read()

    passwords: list[str] = []

    while len(passwords) < 2:
        pwd = incrementPassword(pwd)
        if passwordCompliance(pwd): passwords.append(pwd)
    return passwords

if __name__ == "__main__": print(main())