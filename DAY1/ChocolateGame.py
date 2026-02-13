input_data=input("Enter Dimensions (n,M):")
n,m=input_data.split()
n=int(n)
m=int(m)
if(n*m)%2==0:
    print("Yes")
else:
    print("No")
