def capitalize_1(string):
#     capitalized_string = string[0].upper()
#     for i in range(1, len(string)-1):
#         if string[i-1] == " ":
#             string[i] = string[i].upper()
#         capitalized_string += string[i]
#     return capitalized_string

# #print(capitalize_1("this is a sentence."))

# def capitalize_2(string):
#     retval = ""
#     string_list = string.split()
#     for word in string_list:
#         word = word[0].upper() + word[1::] + " "
#         retval += word
#     return retval

# print(capitalize_2("this is a sentence."))

# # Element comprehension with capitalize()
# def capitalize_3(string):
#     retval = ""
#     string_list = string.split()
#     for word in string_list:
#         word = word[0].upper() + word[1::] + " "
#         retval += word
#     return retval

# print(capitalize_3("this is a sentence."))