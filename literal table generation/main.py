def generate_literal_table_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        source_code = file.read()

    literal_table = {}
    location_counter = 0

    # First Pass
    for line in source_code.split('\n'):
        if line.strip() == '':
            continue

        parts = line.split()
        opcode = parts[0]

        if opcode == 'START':
            location_counter = int(parts[1])
        elif opcode == 'END':
            break
        elif opcode == 'DS' or opcode == 'DC':
            location_counter += int(parts[2])
        elif opcode == 'READ' or opcode == 'MOVER' or opcode == 'ADD' or opcode == 'SUB' or opcode == 'COMP':
            for part in parts[1:]:
                if part.startswith('='):
                    literal = part[2:-1]  # Remove quotes
                    if literal not in literal_table:
                        literal_table[literal] = location_counter
                        location_counter += 1

    # Second Pass
    for line in source_code.split('\n'):
        if line.strip() == '':
            continue

        parts = line.split()
        opcode = parts[0]

        if opcode == 'END':
            break
        elif opcode == 'READ' or opcode == 'MOVER' or opcode == 'ADD' or opcode == 'SUB' or opcode == 'COMP':
            for part in parts[1:]:
                if part.startswith('='):
                    literal = part[2:-1]  # Remove quotes
                    print(f'{literal}\t{literal_table[literal]}')

# Example usage
file_path = 'input3.txt'
generate_literal_table_from_file(file_path)
