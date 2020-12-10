def countVowels(string):
	count = 0
	for ch in string:
		if ch in "aeiouAEIOU":
			count +=1 
	return count 

# Main code 
# function calls
ans="y"
while (ans=="y"):
    string=str(input("Enter a string:"))
    print ("No. of vowels are {0} in \"{1}\"".format(countVowels(string),string))
    ans=str(input("Enter:\n1. y for yes\n2. Any Key for exit.\n"))

