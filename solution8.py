def calculate_average_monthly_steps(input_file, output_file):
    months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    monthly_steps = [0] * 12
    with open(input_file, 'r') as input_f:
        for i, line in enumerate(input_f):
            monthly_steps[i // 31] += int(line)
    with open(output_file, 'w') as output_f:
        for average in [steps // days for steps, days in zip(monthly_steps, months_days)]:
            output_f.write(f'{average}\n')

calculate_average_monthly_steps('input8.txt', 'output8.txt')
