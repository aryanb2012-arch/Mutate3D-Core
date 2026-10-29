def check_frameshift (original_seq, mutated_seq):
    cleaned_orig = original_seq.strip().upper().replace("\n","")
    cleaned_mut = mutated_seq.strip().upper().replace("\n","")
    len_diff = len(cleaned_mut) - len(cleaned_orig)
    if len_diff % 3 == 0:
        return False
    else:
        return True

if __name__ == "__main__":
    test_orig = "AUGUUUCCGCUAG"
    test_inframe = "AUGCCGCUAG"     # Deleted 3 bases (no frameshift)
    test_frameshift = "AUGUUCCGCUAG" # Deleted 1 base (frameshift!)

    print("Test 1 (In-frame expected False):", check_frameshift(test_orig, test_inframe))
    print("Test 2 (Frameshift expected True):", check_frameshift(test_orig, test_frameshift))