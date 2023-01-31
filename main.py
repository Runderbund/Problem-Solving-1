"""
Task 1: Reverse a String
Write code that takes a string as input and returns the string reversed
i.e. “Hello” will be returned as “olleH”
1. Start an empty String ""
2. Loop through word backward char by char and add to String

1. Reverse string slice
"""
def reverse_string_by_loop(string):
    reversed_string = ""
    for char in range(len(string)-1, -1, -1):
        reversed_string += string[char]
    return reversed_string

#print (reverse_string_by_loop("Hello"))

def reverse_string_by_slice(string):
    reversed_string = string[::-1]
    #Goes from start 0 to end len(string) in reverse
    return reversed_string

#print (reverse_string_by_slice("Hola"))

"""
Task 2: Capitalize a Letter
Write code that takes a string as input and capitalize the first letter of each word. Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”

1. Split on " "
2. Capitalize all in list
3. Concatenate list back to string

1. Use join and element comprehension on a split

1. Use the title() function
"""

def capitalize_1(string):
    retval = ""
    string_list = string.split()
    for word in string_list:
        word = word[0].upper() + word[1::] + " "
        retval += word
    return retval

# print(capitalize_1("this is a sentence."))

# Element comprehension with capitalize()
def capitalize_2(string):
    return " ".join(word.capitalize() for word in string.split())

#print(capitalize_2("this is a sentence."))

# Use title()
def capitalize_3(string):
    return string.title()

#print(capitalize_3("this is a sentence."))

"""
Task 3: Palindrome
A “palindrome” is a word, phrase, or sequence that reads the same backward as forward i.e. madam	
Write code that takes a user input and checks to see if it is a Palindrome and reports the result

1. Use string slicing to reverse string
2. Check whether strings match
"""

def check_for_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

# print(check_for_palindrome("String"))
# print(check_for_palindrome("Wow")) #False if comparing cases
# print(check_for_palindrome("wow")) 
# print(check_for_palindrome("tacocat"))

"""
Bonus Challenge
Task 4 : Compress a string of characters
For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a"

1. Start counter at 1
2. Increase counter each time string[i] matches string[i+1]
"""

def compress_string(string):
    count = 1
    compressed_string = ""
    for i in range(len(string)-1): # Will be comparing one forward, avoid index error at end
        if string[i] == string[i+1]:
            count +=1
            if i == len(string)-2:
                compressed_string += str(count) + string[i]
        else:
            compressed_string += str(count) + string[i]
            count = 1
    return compressed_string


print (compress_string("aaabbbbbccccaacccbbbaaabbbaaa"))