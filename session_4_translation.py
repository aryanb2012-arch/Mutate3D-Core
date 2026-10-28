def translate_codon(codon):
    codon_table = {
        "AUG": "M", "UUU": "F", "UUC": "F", 
        "GCU": "A", "GCC": "A", "UAG": "STOP", 
        "UAA": "STOP", "UGA": "STOP", "UCC": "S", "UCU": "S", "UCA": "S", "UCG": "S"
    }
    return codon_table.get(codon,"Unknown")

def translate_sequence(rna_sequence):
    if len(rna_sequence) % 3 != 0:
        return "Error: Sequence is not divisible by 3"

    protein = []
    started = False
    
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        
        if not started:
            if codon == "AUG":
                started = "True"
            else:
                continue
        
        amino_acid = translate_codon(codon)
        
        if amino_acid == "STOP":
            break
    
        protein.append(amino_acid)
    
    return "-".join(protein)

if __name__ == "__main__":
    test_strand = "GCUAUGUUUUUCGCCUAG"
    print("RNA Strand:   ", test_strand)
    print("Protein Chain:", translate_sequence(test_strand))