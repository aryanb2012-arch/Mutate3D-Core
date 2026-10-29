def check_frameshift (original_seq, mutated_seq):
    cleaned_orig = original_seq.strip().upper().replace("\n","")
    cleaned_mut = mutated_seq.strip().upper().replace("\n","")
    len_diff = len(cleaned_mut) - len(cleaned_orig)
    if len_diff % 3 == 0:
        return False
    else:
        return True
def find_divergence_index(orig_protein, mut_protein):
    min_len = min((len(orig_protein)), len(mut_protein))
    for i in range (0, min_len, 1):
        if orig_protein[i] != mut_protein[i]:
            return i + 1
    return -1

if __name__ == "__main__":
    
    test_orig = "AUGUUUCCGCUAG"
    test_inframe = "AUGCCGCUAG"
    test_frameshift = "AUGUUCCGCUAG"

    print("Test 1 in-frame:", check_frameshift(test_orig, test_inframe))
    print("Test 2 frameshift:", check_frameshift(test_orig, test_frameshift))

    
    orig_protein = "MFPL"
    mut_protein = "MFR"  
    
    div_idx = find_divergence_index(orig_protein, mut_protein)
    print(f"Test 3 divergent index: {div_idx}")