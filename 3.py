str1=input("Please enter the string: ")
dict1 ={i:0 for i in str1}

for i in str1:
    count=dict1.get(i)
    count+=1
    dict1.update({i:count})
print(dict1)
min=dict1.get(str1[0])
for i in dict1.values():
    if(i<min):
        min=i
key_list=list(dict1.keys())
val_list=list(dict1.values())
position=val_list.index(min)
print(key_list[position])
    

