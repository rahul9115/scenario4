str1=input("Please enter the string: ")
dict1 ={i:0 for i in str1}
for i in str1:
    count=dict1.get(i)
    count+=1
    dict1.update({i:count})
val=0
k=False
if len(set(dict1.values()))==1:
    k=True
    print("Frequency already matches")
else:
    while True:
        a=input("Enter a character: ")
        a=a.strip()
        if(len(a)!=1 or a.isdigit()):
            print("Enter only a character: ")
            continue
        else:
            val+=1
            if(val==5):
                break
            else:
                try:
                    count=dict1.get(a)
                    count+=1
                    dict1.update({a:count})
                except:
                    continue
                print(set(dict1.values()))
                if len(set(dict1.values()))==1:
                    print("Now the frequency matches")
                    k=True
                    break
if(k==False):
    print("Frequency didn't match")


