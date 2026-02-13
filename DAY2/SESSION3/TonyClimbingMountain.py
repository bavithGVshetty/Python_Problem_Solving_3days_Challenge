def climbing_stairs(N):
    if (N==0 or N==1):
        return 1
    
    return climbing_stairs(N-1)+climbing_stairs(N-2)

N=int(input("Enter the Number of Stairs\n"))
print(climbing_stairs(N))