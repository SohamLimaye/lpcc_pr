def generate_mnt(input_file):
    mnt = {}
    with open(input_file, 'r') as file:
        current_macro = None
        for line in file:
            parts = line.strip().split()
            if len(parts) >= 2 and parts[0] == "MACRO":
                macro_name = parts[1]
                if macro_name not in mnt:
                    mnt[macro_name] = {"MDT_index": len(mnt) + 1, "no_of_parameters": len(parts) - 2}
                current_macro = macro_name
            elif current_macro and parts[0] == "MEND":
                current_macro = None
    return mnt

input_file = "input.txt"
mnt = generate_mnt(input_file)

print("Macro Name Table (MNT):")
print("{:<15} {:<15} {:<15}".format("Macro Name", "MDT Index", "# of Parameters"))
for macro_name, details in mnt.items():
    print("{:<15} {:<15} {:<15}".format(macro_name, details["MDT_index"], details["no_of_parameters"]))
