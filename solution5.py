def perform_operation(input_file, output_file):
  with (open(input_file, encoding='utf-8') as in_f,
        open(output_file, 'w') as out_f):
    try:
      num1, num2, num3 = map(int, in_f.readline().split())
      if num1 == 0 or num2 == 0 or num3 == 0:
        raise ZeroDivisionError('Division by 0')
      result = num1 / num2 + num3
      out_f.write(f'{result:.1f}')
    except ValueError:
      out_f.write('Data error')
    except ZeroDivisionError as e:
      out_f.write(e)

input_file = 'input5.txt'
output_file = 'output5.txt'
perform_operation(input_file, output_file)


