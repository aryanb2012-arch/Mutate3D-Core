from session_4_translation import translate_sequence
from session_7_frameshift import check_frameshift, find_divergence_index

def analyze_mutation_pipeline (orig_mrna, mut_mrna):
    orig_prot = translate_sequence(orig_mrna)
    mut_prot = translate_sequence(mut_mrna)
    is_frameshift = check_frameshift(orig_mrna, mut_mrna)
    divergence_pos = find_divergence_index(orig_prot, mut_prot)
    return {
        "original_protein": orig_prot,
        "mutated_protein": mut_prot,
        "is_frameshift": is_frameshift,
        "divergence_position": divergence_pos
    }

if __name__ == "__main__":
    orig_1 = "AUGUUUUUCCCCUAG"  
    mut_1  = "AUGUUCCCCUAG"     
    print("Test 1 (3-base deletion):", analyze_mutation_pipeline(orig_1, mut_1)["is_frameshift"])

    orig_2 = "AUGUUUUUCCCCUAG"  
    mut_2  = "AUGUUUUCCCCUAG"   
    print("Test 2 (1-base deletion):", analyze_mutation_pipeline(orig_2, mut_2)["is_frameshift"])