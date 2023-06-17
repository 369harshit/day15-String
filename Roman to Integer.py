def roman_to_integer(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0

    for i in range(len(roman) - 1, -1, -1):
        current_value = roman_dict[roman[i]]
        if current_value >= prev_value:
            result += current_value
        else:
            result -= current_value
        prev_value = current_value

    return result

# Example usage
roman_numeral = "III"
integer_value = roman_to_integer(roman_numeral)
print(integer_value)
