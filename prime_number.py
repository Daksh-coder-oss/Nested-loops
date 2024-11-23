uppernum=int(input("Please enter a number"))
lowernum=int(input("Please enter a number"))



for i in range(lowernum,uppernum+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
