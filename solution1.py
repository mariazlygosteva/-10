def convert_to_uppercase(input_file, output_file):
    with (open(input_file, encoding='utf-8') as infile,
          open(output_file, 'w') as outfile):
        for line in infile:
            uppercase_line = line.upper()
            outfile.write(uppercase_line)

input_file = 'input1.txt'
output_file = 'output1.txt'
convert_to_uppercase(input_file, output_file)
