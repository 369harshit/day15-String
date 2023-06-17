def atoi(s):
    # Remove leading whitespace
    s = s.strip()

    # Check if the string is empty
    if len(s) == 0:
        return 0

    # Check if the string starts with a sign (+ or -)
    sign = 1
    if s[0] == '+' or s[0] == '-':
        if s[0] == '-':
            sign = -1
        s = s[1:]  # Remove the sign from the string

    # Convert the remaining characters to an integer
    result = 0
    for char in s:
        # Check if the character is a digit
        if not char.isdigit():
            break  # Stop conversion if a non-digit character is encountered
        result = result * 10 + int(char)

    # Apply the sign to the result
    result *= sign

    return result

# Example usage
string_num = "   -42  with words  "
integer_num = atoi(string_num)
print(integer_num)
