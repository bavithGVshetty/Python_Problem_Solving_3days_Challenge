tuple_list=eval(input("Enter the list of tuples:"))
k=int(input("Enter the k value:"))
# [(1,2,3),(5,4,3),(9,0,6)]
product=1

valid =True
if( k<0 and k>len(tuple_list)):
    print("Invalid")
    valid=False
 
for tup in tuple_list:
    if k < len(tup):
        product *=tup[k]
    else:
        print("Invalid k value")
        valid=False
        break
    
if valid:
    print(f"Product of values in column {k}: {product}")