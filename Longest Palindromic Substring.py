def is_palindrome(string):
    return string == string[::-1]

def longest_palindromic_substring(string):
    n = len(string)
    longest_palindrome = ""
    max_length = 0

    for i in range(n):
        for j in range(i, n):
            substring = string[i:j+1]
            if is_palindrome(substring) and len(substring) > max_length:
                max_length = len(substring)
                longest_palindrome = substring

    return longest_palindrome

# Example usage
input_string = "babad"
result = longest_palindromic_substring(input_string)
print(result)
