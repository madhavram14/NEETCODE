#https://neetcode.io/problems/duplicate-integer/history?list=neetcode150&submissionIndex=1

#The problem was to return true if there are duplicates in the list and false if not
#To do this I used the concept of set
seen=set()#We create a set
for num in nums:#We iterate through all elements in the list using power of python code
    if num in seen:#if the iteration is in the set meaning repetition
        return True
    seen.add(num)#if not present, it gets added to the set
return Falsegit 