tuple1=(1,0,1,1,0,0,0)
Chances = 0
rainy=0
sunny=0
for chances in tuple1:
    if tuple1[Chances] == 1:
        rainy+=1
    else:
        sunny+=1
    Chances+=1

if rainy>sunny:
    print("It will rain today")
else:
    print("It will be a sunny day")