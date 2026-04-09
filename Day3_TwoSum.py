https://neetcode.io/problems/two-integer-sum/question
#In this problem we are to check adding which 2 numbers inside an array we get target and then return those indices in ascending order
nums=[3,4,5,6]
target=7
for i in range(len(nums)):#the first element
    for j in range(i):# the next value
        k=[j,i]# only because j will be less than i and they have asked indices in ascending order
        c=nums[i]+nums[j]#if we add up the values in i and j index
        if c==target:
            return k
        
