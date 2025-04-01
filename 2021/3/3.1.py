nums=[]

while True:
    try:
        nums.append(str(input("Enter Binary Value: ")))
    except KeyboardInterrupt:
        break

common_bits=[]
epsilon_bits=""
gamma_bits=""

for i in zip(*nums):
    if i.count("1")<i.count("0"):
        epsilon_bits+="1"
    else:
        epsilon_bits+="0"

for i in zip(*nums):
    if i.count("1")>i.count("0"):
        gamma_bits+="1"
    else:
        gamma_bits+="0"

print("EPSILON",epsilon_bits)
print("GAMMA",gamma_bits)

print(int(epsilon_bits,2)*int(gamma_bits,2))