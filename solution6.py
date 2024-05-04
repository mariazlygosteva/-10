def check_line_count(input_file, output_file):
    try:
        with (open(input_file, encoding='utf-8') as input_f,
              open(output_file, 'w') as output_f):
            line_count = int(input_f.readline())
            actual_line_count = sum(1 for line in input_f)
            if actual_line_count == line_count:
                output_f.write('YES')
            else:
                output_f.write('NO')
    except ValueError:
        with open(output_file, 'w') as output_f:
            output_f.write('ERROR')
check_line_count('input6.txt', 'output6.txt')
