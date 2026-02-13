products=eval(input("Enter the dictionary"))
sort_by=input("Key/Price: ").strip().upper()
# Key,kEy,k!=K

# {'Laptop': 800, 'Mobile': 400, 'TV': 600,'Headphones': 100}
if sort_by=='KEY':
    sorted_dict=dict(sorted(products.items()))
elif sort_by=="PRICE":
    sorted_dict=dict(sorted(products.items(),key=lambda item:item[1]))
else:
    sorted_dict=products
    print("Inavlid sort option")
print("Sorted Dictionary: ",sorted_dict)