# 6 Exercise
# File Handling

# Write a program that reads a text file and inserts line numbers in front of each of its lines and counts all the letters
# and punctuation marks. The result should be written to another text file.

with open ("text.txt") as file:
    content = [line.strip() for line in file.readlines()]
    new_file_lines = []
    for line_numb in range(0, len(content)):
        count_punct = 0
        for punct in content[line_numb]:
            if punct in r'-,\.!?\'':
                count_punct += 1
        new_file_lines.append(f"Line {line_numb + 1}: {content[line_numb]} ({sum([len(word) for word in content[line_numb].split()]) - count_punct}) ({count_punct})")

    with open("output.txt", "w") as out_file:
        out_file.writelines([line + "\n" for line in new_file_lines])