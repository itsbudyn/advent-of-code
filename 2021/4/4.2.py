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

vboards=[]
vline=0
lastcall=0
vmatches=0

while len(matches)!=len(draws):
    for board in boards:
        for j in range(5):
            score_x=0
            score_y=0
            for i in board[j]:
                if i in matches:
                    score_x+=1
                    if score_x==5:
                        if board not in vboards:
                            vline=board[j]
                            vboards.append(board)
                            lastcall=int(matches[-1])
                            vmatches=matches[:]
            for i in list(zip(*board))[j]:
                if i in matches:
                    score_y+=1
                    if score_y==5: 
                        if board not in vboards:
                            vline=list(zip(*board))[j]
                            vboards.append(board)
                            lastcall=int(matches[-1])
                            vmatches=matches[:]
    matches.append(draws[len(matches)])

vboard=vboards[-1]

print(vmatches)
print(vboard)

nsum=0
for i in vboard[:]:
    for l in i:
        if l not in vmatches: nsum+=int(l)
        
print("Sum of remaining",nsum)
print("Last called",lastcall)
print("Answer",int(int(nsum)*lastcall))