from session_6_file_reader import read_fasta_file
from session_5_summary import generate_summary
from session_4_translation import translate_sequence

# The mutation scanner logic lives here
orig_header, original = read_fasta_file("sequence.fasta")
mut_header, mutated = read_fasta_file("mutate.fasta")

print(f"--- Analysing {orig_header} vs {mut_header} ---")

if len(original) == len(mutated):
    mutation_count = 0
    for i in range(0, len(original), 3):
        orig_codon = original[i:i+3]
        mut_codon = mutated[i:i+3]
        if orig_codon != mut_codon:
            codon_num = (i//3 + 1)
            print(f"Mutation found at codon {codon_num} (Position {i+1}-{i+3}): {orig_codon} -> {mut_codon}")
            mutation_count += 1
    orig_protein = translate_sequence(original)
    mut_protein  = translate_sequence(mutated)
    if orig_protein == mut_protein:
        mutation_type = "Silent Mutation"
    elif "Stop" in mut_protein and "Stop" not in orig_protein:
        mutation_type = "Nonsense Mutation"
    else:
        mutation_type = "Missense Mutation"
    
    generate_summary(len(original), mutation_count, mutation_type, orig_protein, mut_protein)
            
else:
    print(f"Error: Sequences must be of same length")    
