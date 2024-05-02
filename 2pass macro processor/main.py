def first_pass(input_file):
    macro_table = {}
    with open(input_file, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if 'MACRO' in line:
                macro_name, arguments = line.split()[1], line.split()[2:]
                macro_table[macro_name] = {'arguments': arguments, 'definition': []}
                while 'MEND' not in lines[i]:
                    macro_table[macro_name]['definition'].append(lines[i])
                    i += 1
                macro_table[macro_name]['definition'].append(lines[i])  # Include MEND line
    return macro_table

def second_pass(input_file, macro_table):
    intermediate_code = []
    with open(input_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if 'MACRO' not in line and 'MEND' not in line:
                for macro_name in macro_table.keys():
                    if macro_name in line:
                        args = line.split()[1:]
                        macro_def = macro_table[macro_name]['definition']
                        for i, arg in enumerate(macro_table[macro_name]['arguments']):
                            for j, l in enumerate(macro_def):
                                macro_def[j] = macro_def[j].replace(arg, args[i])
                        intermediate_code.extend(macro_def[1:-1])  # Exclude MACRO and MEND lines
                        break
            else:
                intermediate_code.append(line)
    return intermediate_code

def write_intermediate_code(intermediate_code):
    with open('intermediate_code.txt', 'w') as file:
        for line in intermediate_code:
            file.write(line)

input_file = 'input.txt'
macro_table = first_pass(input_file)
intermediate_code = second_pass(input_file, macro_table)
write_intermediate_code(intermediate_code)
