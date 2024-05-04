import os

def process_file(input_file, output_dir):
  os.makedirs(output_dir, exist_ok=True)
  output_file = os.path.join(output_dir, 'output9.txt')
  with open(input_file, encoding='utf-8') as in_f, open(output_file, 'w') as out_f:
    line_num = 0
    for line in in_f:
      line_num += 1
      if line_num % 2 == 0:
        out_f.write(line)

input_file = 'input9.txt'
output_file = 'simple'
process_file(input_file, output_file)



