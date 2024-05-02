def first_pass(lines):
    symbol_table = {}
    location_counter = 0

    for line in lines:
        line = line.strip()
        if line:
            parts = line.split()
            if len(parts) > 1:
                if parts[1] == 'EQU':
                    symbol_table[parts[0]] = int(parts[2])
                else:
                    symbol_table[parts[0]] = location_counter
                    location_counter += 1
            else:
                location_counter += 1

    return symbol_table


def second_pass(lines, symbol_table):
    pool_table = []
    location_counter = 0

    for line in lines:
        line = line.strip()
        if line:
            parts = line.split()
            if len(parts) > 1:
                if parts[1] != 'EQU':
                    pool_table.append((location_counter, parts))
                    location_counter += 1

    return pool_table


def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    symbol_table = first_pass(lines)
    pool_table = second_pass(lines, symbol_table)

    print("Symbol Table:")
    for symbol, value in symbol_table.items():
        print(f"{symbol}\t{value}")

    print("\nPool Table:")
    for entry in pool_table:
        print(entry[0], end="\t")
        for part in entry[1]:
            print(part, end="\t")
        print()


if __name__ == "__main__":
    main()
