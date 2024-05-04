input_file = "input10.txt"
output_file = "output10.txt"

with open(input_file, encoding='utf-8') as file:
    date = file.readline().strip().split('.')
    current_day, current_month = map(int, date)
    num_cells = int(file.readline().strip())
    cell_info = [line.strip().split() for line in file]
stored_more_than_3_days = []

for cell_data in cell_info:
    cell_number, stored_date = cell_data
    stored_day, stored_month = map(int, stored_date.split('.'))
    days_store = (current_day + current_month * 30) - (stored_day + stored_month * 30)
    if days_stored > 3:
        stored_more_than_3_days.append(cell_number)

with open(output_file, 'w') as file:
    for cell_number in stored_more_than_3_days:
        file.write(cell_number)



