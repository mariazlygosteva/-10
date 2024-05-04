def filter_lines(input_file, output_file):
  with (open(input_file, encoding='utf-8') as infile,
        open(output_file, 'w') as outfile):
    for line in infile:
      if line.upper().startswith('A'):
        outfile.write(line)

input_file = 'input2.txt'
output_file = 'output2.txt'
filter_lines(input_file, output_file)
