def generate_summary(seq_length, mutation_count, mutation_type, orig_protein, mut_protein):
    print("\n--- MUTATE3D SUMMARY REPORT ---")
    print(f"Sequence Length: {seq_length}")
    print(f"Total Mutations Found: {mutation_count}")
    print(f"Mutation Type: {mutation_type}")
    print(f"Original: {orig_protein} -> Mutated: {mut_protein}")
    print("-------------------------------")