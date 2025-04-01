movements=[]
hpos=0
aim=0
depth=0

while True:
    try:
        x=input("Enter direction and distance: ")
    except KeyboardInterrupt:
        break

    direction=x.split(" ")
    direction[1]=int(direction[1])
    movements.append(direction)


for i in movements:
    print(i)
    match i[0]:
        case "forward":
            hpos+=i[1]
            depth+=(i[1]*aim)
        case "down":
            aim+=i[1]
        case "up":
            aim-=i[1]

print("HPOS",hpos,"\nDEPTH",depth,"\nPRODUCT",hpos*depth)