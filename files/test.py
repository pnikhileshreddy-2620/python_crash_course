input_path = 'C:/Users/pongredd/Downloads/EOB.txt'
output_path = 'C:/Users/pongredd/Downloads/EOB_modified.txt'

with open(input_path, 'r') as file_object:
    lines = file_object.readlines()

with open(output_path, 'w') as output_file:
    for line in lines:
        modified_line = line.replace(' ', ' | ')
        output_file.write(modified_line)
        print(modified_line)