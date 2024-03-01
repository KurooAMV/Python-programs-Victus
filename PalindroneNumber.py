n=int(input("Enter the number: "))
#n=12321
f=n
m=0
while n>0:
   r=n%10
   n=n//10
   m=(m*10)+r
if m==f:
    print(f"The number {f} is a Palindrone number.")
else: 
    print(f"{f} is not a Plaindrone number.")
