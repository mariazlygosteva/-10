def remove_lines_with_100(filename):
  with open(filename, 'r+', encoding='utf-8') as f:
    lines = f.readlines()
    f.seek(0)
    f.writelines(line for line in lines if str(100) not in line)
    f.truncate()

remove_lines_with_100('input7.txt')

