def read_sequence_file(filename):
    with open(filename, "r") as file:
        sequence = file.read().strip()
    return sequence

def read_fasta_file(filename):
    sequence = ""
    header = ""
    with open(filename, "r") as file:
        for line in file:
            clean_line = line.strip()
            if clean_line.startswith(">"):
                header = clean_line[1:]
                continue
            else:
                sequence += clean_line
    return header, sequence

my_sequence = read_sequence_file("sequence.txt")
print(f"Successfully loaded sequence: {my_sequence}")

header, my_second_sequence = read_fasta_file("sequence.fasta")
print(f"Successfully loaded sequence: {my_second_sequence}")
print(f"Header: {header}")
