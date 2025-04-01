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

digits=[0,1,2,3,4,5,6,7,8,9]
digits[0]="abcefg"
digits[1]="cf"
digits[2]="acdeg"
digits[3]="acdfg"
digits[4]="bcdf"
digits[5]="abdfg"
digits[6]="abdefg"
digits[7]="acf"
digits[8]="abcdefg"
digits[9]="abcdfg"

matches=0
for i in entry:
    for j in i:
        match len(j):
            case 2: matches+=1
            case 3: matches+=1
            case 4: matches+=1
            case 7: matches+=1
        
print(matches)