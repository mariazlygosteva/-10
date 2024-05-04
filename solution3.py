def get_word_from_first_chars(input_file, output_file):
  with (open(input_file, encoding='utf-8') as infile,
        open(output_file, 'w') as outfile):
    word = ""
    for line in infile:
      word += line[0]
    outfile.write(word)

input_file = 'input3.txt'
output_file = 'output3.txt'
get_word_from_first_chars(input_file, output_file)
