# Python3 program for the above approach
# Count all the frequencies of 1st and 2nd strings and using counter()
# If they are equal then print anagram
from collections import Counter

# function to check if two strings are
# anagram or not
def find_anagram(s1, s2):

	# implementing counter function
	if(Counter(s1) == Counter(s2)):
		print("The strings are anagrams.")
	else:
		print("The strings aren't anagrams.")


# driver code
s1 = "listen"
s2 = "silent"
find_anagram(s1, s2)
