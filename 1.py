l=[]
for i in range(5):
    t=()
    a=""
    b=0
    while True:
        a=input("Enter a string: ")
        if(len(a)<2):
            print("Please enter valid input")
            continue
        
        break
    while True:
        b=input("Enter a number: ")
        if(b.isdigit()==False):
            print("Please enter valid input")
            continue
        
        break
    t=(a,int(b))
    l.append(t)
print(l)
new_t=()
dummy=()
for i in range(1,len(l)):
    left=i-1
    dummy=l[i]
    while(left>=0):
        if(dummy[1]<l[left][1]):
            l[left+1]=l[left]
        else:
            break
        left-=1
    l[left+1]=dummy
print("After insertion sort: ",l)
new_list=[]
new_list_1=[]
new_list_2=[]
import math

for i in l:
    k=0
    
    for j in range(2,int(math.sqrt(i[1]))+1):
        if(i[1]%j==0):
            k+=1
            break
    if(k==1):
        
        new_list_1.append(i[0])
        new_list_1.append(i[1])
    else:
        new_list_1.append(i[0])
        new_list_2.append(i[1])
new_list.append(tuple(new_list_1))
new_list.append(tuple(new_list_2))
print(new_list)

    
