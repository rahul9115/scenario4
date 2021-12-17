str1=input("Please enter the string: ")
s=str1.split(" ")
str2=""
for i in s:
    if(len(i)<=4):
        s.remove(i)
str1=' '.join(s)
print(str1)

