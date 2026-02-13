input=input("Enter a name: ")
mid=len(input)//2
firstHalf=input[:mid]
secondHalf=input[mid:]
rev_firstHalf=firstHalf[::-1]
rev_secondHalf=secondHalf[::-1]
result=rev_firstHalf+rev_secondHalf
print(result)