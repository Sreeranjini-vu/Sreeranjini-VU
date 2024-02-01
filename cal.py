print("CALCULATOR\n 1.ADD\n 2.SUBSTRACT\n 3.MULTIPLICATION\n 4.DIVISION\n")
n=int(input("enter the choices:"))
if(n==1):
    a=int(input("enter the first no:"))
    b=int(input("enter the second no:"))
    c=a+b
    print("sum is",c)
elif(n==2):
    a=int(input("enter the first no:"))
    b=int(input("enter the second no:"))
    c=a-b
    print("subsracted value is",c)
elif(n==3):
    a=int(input("enter the first no:"))
    b=int(input("enter the second no:"))
    c=a*b
    print("multiplied value is",c)
elif(n==4):
    a=int(input("enter the first no:"))
    b=int(input("enter the second no:"))
    c=a/b
    print("divided value is",c)
else:
    print("invalid operation")
    
    