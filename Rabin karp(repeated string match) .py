def repeated_string_match(A, B):
    # Find the minimum number of times A needs to be repeated to contain B
    min_repeats = (len(B) - 1) // len(A) + 1                                             #  8-1 ie.7/5 ---> remainder = min_repeats=2

    # Repeat A the minimum number of times
    repeated_A = A * min_repeats

    # Check if repeated_A contains B
    if B in repeated_A:
        return min_repeats

    # Check if adding one more repetition of A contains B
    if B in repeated_A + A:
        return min_repeats + 1

    # B is not a substring of A
    return -1

# Example usage
A = "a"
B = "aa"
repeats = repeated_string_match(A, B)
print(repeats)
