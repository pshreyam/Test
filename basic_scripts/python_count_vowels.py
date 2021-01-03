def count_vowels(string):
	count = 0
	for ch in string:
		if ch in "aeiouAEIOU":
			count += 1 
	return count 

# main code 

ans = "y"
while ans == "y":
    string=str(input("Enter a string:"))
    print ("No. of vowels are {0} in \"{1}\"".format(count_vowels(string), string))
    ans = str(input("Enter:\n1. y for yes\n2. Any Key for exit.\n"))
