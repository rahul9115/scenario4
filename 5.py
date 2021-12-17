#string="didisdiss"
string=input("Enter a string: ")
sub=input("Enter a sub-string: ")
output=string.replace(sub,'')
if(output==sub):
    print("Recursive deletion is possible.String after deletion is empty")
else:
    print(f"Recursive deletion is not possible.String after deletion is {output}")


