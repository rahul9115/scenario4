import datetime
eusers=[]

print("Enter 1 to add user, 2 to remove user")
n=int(input())
print("Enter the username to add or remove, date(yyyy-mm-dd),time(hr:mins:sec): ")
user=list(map(str,input().split(", ")))
print(user)
date=datetime.datetime.strptime(user[1]+" "+user[2],'%Y-%m-%d %H:%M:%S')
date_now=datetime.datetime.now()
if(n==1):
    
    if(date>date_now):
        print(f"User will be successfully be added on {user[1]} at {user[2]}")
        

    elif(date==date_now):
        print("User sucessfully added")
        eusers.append(user[0])
        
        
    else:
        print("User cannot be added as its a past date")
        
if (n==2):
    if(date>date_now):
        print(f"User will be successfully removed on {user[1]} at {user[2]}")
        
    elif(date==date_now):
        print("User sucessfully deleted")
        eusers.remove(user[0])
        
        
    else:
        print("User cannot be deleted as its a past date")
        

    
