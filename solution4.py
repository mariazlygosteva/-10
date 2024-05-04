def process_file(input_file, output_file):
  with (open(input_file, encoding='utf-8') as infile,
        open(output_file, 'w') as outfile):
    for line in infile:
      if len(line.strip()) > 20:
        outfile.write(line)

process_file('input4.txt', 'output4.txt')
