### Algorithm ==========================================================================================================
"""
1. Get a string as an input from the user
2. Save it in a parameter called 'string'
3. Create a parameter start to resemble the start of the loop
4. Initiate 'start' = string's length - 1 to start from the last letter
5. Create a new parameter called 'reverse' and put an empty string in it
6. Loop over the string, starting from its last letter
    6.1. Check if 'start' is still greater than or equals 0 - 0 means that we have reached the first letter in the string
    6.2. if start >= 0:
        6.3.1. Add the letter placed in the index of 'start' to the 'reverse' varialbe
        6.3.2. Decrease the 'start' variable by 1
        6.3.3. Continue the loop
    6.4. If start <0:
        6.4.1. Stop the loop
7. Display the reversed string to the user
    
"""
### Code ================================================================================================================
string = input("Enter a string: ")
start = len(string) - 1
reverse = ""
while start >= 0:
    reverse += string[start]
    start -= 1

print(reverse)
