tuple1= (45,63,93,32,64,543)
even = []
odd=[]
evenproduct=1
oddproduct=1
for i in tuple1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

for i in even:
    evenproduct*=i
print(evenproduct)
for i in odd:
    oddproduct*=i
print(oddproduct)
