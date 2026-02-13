num_series=input("Enter the list of number Series: ").split()
k=int(input("Enter the thrushold\n"))

processed_num=[]

print("The number with freq >k")

for num in num_series:
    if num not in processed_num:
        count=0
        for i in num_series:
            if i==num:
                count+=1
        if count>k:
            print(f"Number {num}:{count} times")
        processed_num.append(num)
