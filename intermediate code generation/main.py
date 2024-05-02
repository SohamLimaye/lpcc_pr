def first_pass(input_file):
    symbol_table = {}
    location_counter = 0

    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith(';'):
                continue

            parts = line.split()
            label = parts[0] if len(parts) > 1 else None
            opcode = parts[-2] if len(parts) > 1 else None
            operand = parts[-1]

            if label:
                symbol_table[label] = location_counter
            if opcode:
                location_counter += 1

    return symbol_table

def second_pass(input_file, symbol_table):
    intermediate_code = []

    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith(';'):
                continue

            parts = line.split()
            label = parts[0] if len(parts) > 1 else None
            opcode = parts[-2] if len(parts) > 1 else None
            operand = parts[-1]

            if opcode:
                if operand in symbol_table:
                    operand = symbol_table[operand]
                intermediate_code.append(f'{opcode} {operand}')

    return intermediate_code

input_file = 'input3.txt'
symbol_table = first_pass(input_file)
intermediate_code = second_pass(input_file, symbol_table)

with open('intermediate_code.txt', 'w') as file:
    for code in intermediate_code:
        file.write(code + '\n')

print('Intermediate code generated successfully.')
