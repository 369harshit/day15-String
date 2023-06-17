def reverse_words(string):
    words = string.split()  # Split the string into a list of words
    reversed_words = words[::-1]  # Reverse the order of the words
    reversed_string = ' '.join(reversed_words)  # Join the reversed words into a string
    return reversed_string

# Example usage
input_string = "this is an amazing program"
reversed_string = reverse_words(input_string)
print(reversed_string)
