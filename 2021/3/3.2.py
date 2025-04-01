def get_most_common_bit(array,pos,favor):
    bits=[0,0]
    for i in array:
        if i[pos]=="0": bits[0]+=1
        else: bits[1]+=1

    if bits[0]>bits[1]: return 0
    elif bits[0]==bits[1]: return favor
    else: return 1

nums=[]
oxygen=[]
scrubber=[]

while True:
    try:
        nums.append(str(input("Enter Binary Value: ")))
    except KeyboardInterrupt:
        break

oxygen=nums[:]
scrubber=nums[:]

for i in range(len(oxygen[0])):
    mcb=get_most_common_bit(oxygen,i,1)
    for j in oxygen[:]:
        if j[i]!=str(mcb) and len(scrubber)!=1: 
            oxygen.remove(j)

for i in range(len(scrubber[0])):
    mcb=get_most_common_bit(scrubber,i,1)
    for j in scrubber[:]:
        if j[i]==str(mcb) and len(scrubber)!=1: 
            scrubber.remove(j)

print(oxygen)
print(scrubber)
print("LSR",int(oxygen[0],2)*int(scrubber[0],2))

"""
for i in nums:
    if i[0]==str(common_bit):
        oxygen.append(i)
    else:
        scrubber.append(i)"""

