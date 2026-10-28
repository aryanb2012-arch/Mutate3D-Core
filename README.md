# Mutate3D 🧬
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A python-based bioinformatics tool designed to translate RNA sequences and analyze point mutations.I am creating a ***3D Mutation Visualizer*** to learn more about Biology, Chemistry and Coding while trying to create a project that is not only fun to make on the way but also can make learning more interactive rather than just textbook learning

## 📌 Project Overview
Mutate3D bridges molecular biology and computer science by simulating how mRNA sequences translate into protein chains and evaluating the impact of genetic mutations.

## ✨ Features
- **RNA Sequence Translator**: Parses mRNA sequences in 3-letter codons to build translated protein chains.
- **Mutation Classifier Engine**: Compares codon pairs to identify and classify single-nucleotide variants into three biological categories:
  - **Silent**: Codon changes, but the translated amino acid remains identical.
  - **Missense**: Codon changes, resulting in a different amino acid.
  - **Nonsense**: Codon changes into a premature **STOP** signal.
- **Gene Sequence Scanner**: Sweeps across complete multi-codon mRNA strands in steps of 3 bases using index math (`range(0, len(seq), 3)`), detecting and logging every mutation's exact sequence position and type.
- **RNA Translation Engine**: Converts codons into amino acids and detects start(AUG) and stop codons(UAG,UAA,UGA)
- **Modular Reporting:** Generates clean, formatted summary reports displaying sequence length, total mutation counts, classification type, and protein chain comparisons.
- **FASTA File Parser:** Dynamically parses standard .fasta files, cleans whitespaces, strips header metadata (>), handles wrapped multiline sequences and returns dual values (header, sequence)

## 🆕 Recent Updates
- **FASTA Parser Integration (`session_6_file_reader.py`)**: 
  - Parses FASTA files dynamically using `.startswith(">")` to strip header metadata from sequence fragments.
  - Cleans whitespace and handles multi-line FASTA streams, outputting a tuple of `(header, sequence)`.
- **Expanded Codon Dictionary**: Added complete Serine family coverage (`UCC`, `UCU`, `UCA`, `UCG`) to resolve full mRNA-to-protein translation without unmapped codons.
- **Dynamic File Ingestion in `main.py`**: Replaced static sequence inputs with live FASTA file parsing, directly piping parsed mRNA strands into the mutation scanner and summary reporter.
- **Position-Specific Codon Diagnostics:** Upgraded the scanner from whole-gene global labels to granular per-codon evaluation (`Codon 2 (Pos 4-6)`).
  
## 💻 Tech Stack
- **Language**: Python 3
- **Core Concepts**: Dictionaries, String Slicing, Step-based Loops, Conditional Logic (`if/elif/else`), Modular Functions,Scope & Modular Architecture (Passing parameters into functions and logging output via `return` values)

## 📁 Project Structure

```text
Mutate3D/
├── main.py                     # Primary entry point & pipeline integration
├── session_4_translation.py    # Translation engine (RNA -> Protein)
├── session_5_summary.py        # Summary report generator
├── session_6_file_reader.py    # FASTA file parser & header extractor
├── sequence.fasta              # Reference RNA sequence
├── mutated.fasta               # Variant RNA sequence
├── LICENSE                     # MIT Open-Source License
└── README.md                   # Project documentation
```

## 🚀 Quick Usage

To run the pipeline on your target sequences:

1. Add your reference sequence to `sequence.fasta` and your variant sequence to `mutated.fasta`.
2. Open your terminal in VS Code and execute:

```bash
python main.py
```

### Example Console Output

```text
--- Analysing original_mRNA vs mutated_mRNA ---
Mutation found at Codon 2 (Pos 4-6): UUU -> UUC
Mutation found at Codon 3 (Pos 7-9): UCC -> GCC
Mutation found at Codon 4 (Pos 10-12): GCC -> UUU

--- MUTATE3D SUMMARY REPORT ---
Sequence Length: 15
Total Mutations Found: 3
Mutation Type: Missense Mutation
Original: M-F-S-A -> Mutated: M-F-A-F
-------------------------------
```