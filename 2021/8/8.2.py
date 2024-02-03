entry=[]
while True:
    try:
        entry.append(str(input("Input: ")).split(" "))
    except KeyboardInterrupt:
        break

for i in range(len(entry)):
    del entry[i][:entry[i].index('|')+1]

for i in range(len(entry)):
    for j in range(len(entry[0])):
        entry[i][j]=''.join(sorted(entry[i][j]))

for i in entry:
    print(i)

values=[]
for i in entry:
    


    num=""
    for j in i:
        match len(j):
            case 2: num+='1'
            case 3: num+='7'
            case 4: num+='4'
            case 7: num+='8'
            case default: 
                
    num=int(num)
    values.append(num)

print(sum(values))