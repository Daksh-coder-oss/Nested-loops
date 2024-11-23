name=input("Please anter a name")
alphabet=input("Please enter what alphabet you want me to find")


count=0
len(name)

for i in range(len(name)):
    if name[i]==alphabet:
        count=count+1
print(count)