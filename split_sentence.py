"""
Split Sentence
Ver. 1.0
1. Create a function called 'split_sentence'
2. The function takes 1 parameter called 'sentence', which represents the sentence to be split
3. The function returns the lst of words in the sentence
---------------------------------------------------------------------
Function Instructions:
1. Check weather the first character in the sentence is a space or not
    1.1. If the first character is a space
    
1. Create a new variable 'start', and initialize it with 0; it will represent the loop start value
2. Create a variable 'lst', and initialize it as an empty list []; it will hold the sentence's words
3. Loop over the sentence, as long as 'start' is less that the sentence's length:
    3.1. Create a new variable called 'word', and initialize it as an empty space
    3.1.If sentence[start] is an empty space:
        3.1.1. If 'word' is empty - which means that no words have been added to the list:
            3.1.1.1. Increase the 'start' varialbe by 1
            3.1.1.2. Continue the loop
        3.1.2. If 'word' is not empty - which means the first character was not a space:
            3.1.2.1. Add the value of 'word' to 'lst'
            3.1.2.2. Empty the variable 'word'
            3.1.2.3. Increate the 'start' variable by one
    3.2. If sentence[start] is not an empty space:
        3.2.1. Add sentence[start] to 'word'
        3.2.2. Increase the 'start' variable by 1
    3.3. If 'start' equals sentence's length - 1:
        3.3.1. Add the value of 'word' to 'lst'
4. Return lst
---------------------------------------------------------------------
Test Data
1. "I have a car"
2. " I have a car"
3. "I  have a   car"
4. " "
            
"""
