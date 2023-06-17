def longest_common_prefix(strs):
    # Check for empty list
    if not strs:
        return ""

    # Initialize the common prefix
    common_prefix = ""

    # Iterate through the characters of the first string
    for i in range(len(strs[0])):
        # Get the current character
        current_char = strs[0][i]

        # Check if the character is common to all strings
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != current_char:
                return common_prefix

        # Add the character to the common prefix
        common_prefix += current_char

    return common_prefix

# Example usage
strings =  ["flower","flow","flight"]
common_prefix = longest_common_prefix(strings)
print(common_prefix)
