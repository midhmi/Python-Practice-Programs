# input string from user
given_string = input()
 
# an empty string variable to store
# the given string in reverse
reverse_string = ""
 
# iterate through the given string
# and append each element of the given string
# to the reverse_string variable
for i in given_string:
    reverse_string = i + reverse_string  
 
# print the reverse_string variable
print(reverse_string)
