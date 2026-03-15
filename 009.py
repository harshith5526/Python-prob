def capitalize_strings(string_list):

# Capitalize each string in the list

return [s.capitalize() for s in string_list]

'''The capitalize() function in Python is used to capitalize the first letter of a string. ''' # Example usage

input_strings = ['hello', 'good', 'how', 'simple']

capitalized_strings = capitalize_strings(input_strings)

print(capitalized_strings)
