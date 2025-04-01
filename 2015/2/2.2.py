def calculateRibbon(arr=[]): 
    for i in range(len(arr)): arr[i] = int(arr[i])
    arr = sorted(arr)
    return 2*arr[0] + 2*arr[1] + arr[0]*arr[1]*arr[2]

def main():
    with open("2.txt","r",encoding="UTF-8") as f: text = f.readlines()
    ribbonAmmount = 0

    for i in text: ribbonAmmount+=calculateRibbon(i.split("x"))
    return ribbonAmmount

if __name__ == "__main__": print(main())