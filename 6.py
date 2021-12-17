lower=False
upper = False
number=False
special=False
print("Enter passwords")
remember=[]
while True:
    x=input()


    
    if (len(x) >= 8):
        for j in x:
            if (j.islower()):
                lower=True			
        
            if (j.isupper()):
                upper=True			

            
            if (j.isdigit()):
                number=True

            if(j.isalpha()==False and j.isdigit()==False):
                special=True
        if (special and number and upper and lower):
            print("Complex Password")
            remember.append(x)
            if(len(remember)==5):
                print("Passwords remembered are: ",remember)
                break
        else:
            print("Simple Password")
    else:
        print("Simple Password")

