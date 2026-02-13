List_of_Ids=input("Enter List of ID: ").split()
Initial_set=set(List_of_Ids)

duplicate_set=set()
for product in List_of_Ids:
    if List_of_Ids.count(product)>1:
        duplicate_set.add(product)
result=Initial_set-duplicate_set
print(result)