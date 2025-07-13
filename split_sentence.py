"""
Split Sentence
Ver. 1.0
1. Create a function called 'split_sentence'
2. The function takes 1 parameter called 'sentence', which represents the sentence to be split
3. The function returns the lst of words in the sentence
---------------------------------------------------------------------
Function Instructions:
1. Create a new variable 'start', and initialize it with 0; it will represent the loop start value
2. Create a variable 'lst', and initialize it as an empty list []; it will hold the sentence's words
3. Create a new variable called 'word', and initialize it as an empty space
4. Loop over the sentence, as long as 'start' is less that the sentence's length:
    4.1.If sentence[start] is an empty space:
        4.1.1. If 'word' is empty - which means that no words have been added to the list:
            4.1.1.1. Increase the 'start' varialbe by 1
            4.1.1.2. Continue the loop
        4.1.2. If 'word' is not empty - which means the first character was not a space:
            4.1.2.1. Add the value of 'word' to 'lst'
            4.1.2.2. Empty the variable 'word'
            4.1.2.3. Increate the 'start' variable by one
    4.2. If sentence[start] is not an empty space:
        4.2.1. Add sentence[start] to 'word'
        4.2.2. Increase the 'start' variable by 1
    4.3. If 'start' equals sentence's length - 1:
        4.3.1. Add the value of 'word' to 'lst'
5. Return lst
---------------------------------------------------------------------
Test Data
1. "I have a car"
2. " I have a car"
3. "I  have a   car"
4. " "
            
"""
start = 0
lst = []
word = "" # Change No.01
sentence = input("Enter a sentence: ")
while start < len(sentence):
    
    if sentence[start] == " ":
        
        if word == "":
            start += 1
            continue

        else:
            lst.append(word) # When we reach the last word, the loop is already finished by then and we can't append the last word to the list
            word = ""
            start += 1

    else:
        word += sentence[start]
        print(word)
        start += 1


    if start == len(sentence) - 1:
        lst.append(word)

print(lst)
