#In this program we are to check if two strings are anagrams. Anagrams are letters mixed up but have the same letters. The way I solved this was sort the 2 strings and then return the boolean. 
#https://neetcode.io/problems/is-anagram/question
def anagram(s,t):
    return(sorted(s)==sorted(t))
#s='racecar'
#t='carrace'
s=input()
t=input()
print(anagram(s,t))