draws=list(input("Enter a number: ").split(","))
input("Newline catch: ")
boards=[]

while True:
    try:
        x=[0,0,0,0,0]
        x[0]=input("Enter line 0: ").split(" ")
        x[1]=input("Enter line 1: ").split(" ")
        x[2]=input("Enter line 2: ").split(" ")
        x[3]=input("Enter line 3: ").split(" ")
        x[4]=input("Enter line 4: ").split(" ")
        for i in x:
            while "" in i:
                i.remove("")    
        boards.append(x)
        input("Newline catch: ").split(" ")
    except KeyboardInterrupt:
        break

matches=draws[0:5]

vboard=0
vline=0
while vboard==0:
    for board in boards:
        for j in range(5):
            score_x=0
            score_y=0
            for i in board[j]:
                if i in matches:
                    score_x+=1
                    if score_x==5:
                        vline=board[j]
                        vboard=board
            for i in list(zip(*board))[j]:
                if i in matches:
                    score_y+=1
                    if score_y==5: 
                        vline=list(zip(*board))[j]
                        vboard=board
            if vboard!=0: break
    if vboard==0:
        matches.append(draws[len(matches)])

print(matches,"\n\n")
for i in vboard:
    print(i)

if vline not in vboard[:]:
    vboard=list(zip(*vboard))

vboard.remove(vline)

nsum=0
for i in vboard:
    for l in i:
        if l not in matches: nsum+=int(l)
print("Sum of remaining",nsum)
print("Last called",matches[-1])
print("Answer",int(int(nsum)*int(matches[-1])))