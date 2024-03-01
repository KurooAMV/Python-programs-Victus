def show(div):
    for i in div:
        print(i)

def find(a,div):
    for i in range(1,a+1):
        if a%i==0:
            div.append(i)

def find2(a,div):
    i=1
    while i*i<=a:
        if a%i==0:
            div.append(i)
            if i!=(a//i):
                div.append(a//i)
        i+=1

def finding(a,div):
    i=1
    while i*i<a:
        if a%i==0:
            div.append(i)
        i+=1
    while i>=1:
        if a%i==0:
            div.append(a//i)
        i-=1
                
num= int(input("Enter the number: "))
div=[]
#find(num,div)
finding(num,div)
#find2(num,div)
if num not in div:
    div.append(num)
print("The divisor of the number ",num," is:")
show(div)