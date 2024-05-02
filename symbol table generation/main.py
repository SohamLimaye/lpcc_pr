def pass_one(lines):
    symbol_table = {}
    location_counter = None
    for line in lines:
        parts = line.split()
        if parts[0] == 'START':
            location_counter = int(parts[1])
        elif parts[0] != 'END':
            if parts[0] not in symbol_table:
                symbol_table[parts[0]] = location_counter
            location_counter += 1
    return symbol_table

def pass_two(lines, symbol_table):
    output = []
    for line in lines:
        parts = line.split()
        if parts[0] != 'START' and parts[0] != 'END':
            if parts[0] in symbol_table:
                output.append(f"{symbol_table[parts[0]]}\t{line}")
            else:
                output.append(f"\t{line}")
    return output

def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    symbol_table = pass_one(lines)
    output = pass_two(lines, symbol_table)

    print("Symbol Table:")
    for symbol, address in symbol_table.items():
        print(f"{symbol}\t{address}")
    
    print("\nOutput Code:")
    for line in output:
        print(line.strip())

if __name__ == "__main__":
    main()
