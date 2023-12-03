def calculateSurface(arr=[]): 
    for i in range(len(arr)): arr[i] = int(arr[i])
    area = 2*arr[1]*arr[0] + 2*arr[0]*arr[2] + 2*arr[2]*arr[1]
    arr = sorted(arr)
    slack = arr[0]*arr[1]
    return area + slack

def main():
    with open("2.txt","r",encoding="UTF-8") as f: text = f.readlines()
    paperAmmount = 0

    for i in text: paperAmmount+=calculateSurface(i.split("x"))
    return paperAmmount

if __name__ == "__main__": print(main())