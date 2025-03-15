def first_non_repeating_character(s):
    # Step 1: Count the frequency of each character
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Step 2: Find the first character with a frequency of 1
    for char in s:
        if frequency[char] == 1:
            return char

    # If no non-repeating character is found, return None or a specific message
    return None


# Example usage:
input_string = "swiss"
result = first_non_repeating_character(input_string)
if result:
    print(f"The first non-repeating character is: {result}")
else:
    print("All characters are repeating.")