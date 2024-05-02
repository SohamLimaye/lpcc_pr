class MacroProcessor:
    def __init__(self):
        self.mdt = {}
        self.mnt = {}

    def first_pass(self, lines):
        mdt_index = 0
        for line in lines:
            if line.startswith("MACRO"):
                macro_name = line.split()[1]
                self.mnt[macro_name] = mdt_index
                self.mdt[mdt_index] = []
                mdt_index += 1
            elif line.startswith("MEND"):
                self.mdt[mdt_index - 1].append(line)
            else:
                self.mdt[mdt_index - 1].append(line)

    def second_pass(self, lines):
        for line in lines:
            if line.startswith("MACRO"):
                macro_name = line.split()[1]
                index = self.mnt[macro_name]
                for mdt_line in self.mdt[index]:
                    print(mdt_line)
            else:
                print(line)

    def generate_mdt(self):
        for index, mdt_lines in self.mdt.items():
            print(f"MDT Index {index}:")
            for line in mdt_lines:
                print(line)
            print()


# Read input from file
with open("input.txt", "r") as file:
    lines = file.readlines()

# Create and process the macro processor
processor = MacroProcessor()
processor.first_pass(lines)
processor.second_pass(lines)

# Generate and print the MDT
processor.generate_mdt()
