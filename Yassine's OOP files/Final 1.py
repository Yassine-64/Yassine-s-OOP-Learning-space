def find_repeated_codes_with_positions(file_path):
    # Dictionary to store occurrences and positions of each code
    code_occurrences = {}

    with open(file_path, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            # Assuming codes are 12 characters long and consist of uppercase letters and digits
            codes = [line[i:i+12] for i in range(len(line) - 11) if line[i:i+12].isalnum() and line[i:i+12].isupper()]

            for code in codes:
                if code in code_occurrences:
                    code_occurrences[code].append(line_num)
                else:
                    code_occurrences[code] = [line_num]

    # Filter codes that occur more than once
    repeated_codes = {code: positions for code, positions in code_occurrences.items() if len(positions) > 1}

    return repeated_codes

file_path = 'Redeem_codes.txt'  # Replace with the path to your actual text file
result = find_repeated_codes_with_positions(file_path)

# Print the occurrences and positions of each repeated code
for code, positions in result.items():
    print(f"Code: {code}, Occurrences at Lines: {positions}")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      