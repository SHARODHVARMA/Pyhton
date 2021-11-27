pocketmoney=int(input("Enter the pocket money you get every month : "))
if(pocketmoney>500):
    print("Your a rich kid")
elif(pocketmoney>100):
    print("You have a good life")
else:
    print("I know what you think now")
f=open("text.txt")
print(f.read())
filelines=f.readlines()
for line in filelines :
    print(line)
name="My name is Sharodh"
words=name.split()
print(words)