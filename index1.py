tuple1=(1,2,3,4,3,3,2,1)
begining = 0
finish = len(tuple1)-1
while finish>begining:
    if tuple1[begining]!=tuple1[finish]:
        print("It is not a palindrome")
        break
    begining+=1
    finish-=1

print("it is a palindrome")