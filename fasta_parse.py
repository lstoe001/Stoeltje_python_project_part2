#!/usr/bin/env python

import sys
from Bio import SeqIO
import pandas as pd

def parse_fasta(fasta_file):
    protein_info = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        seq_id = record.id
        first_10_aa = str(record.seq)[:10]
        length = len(record.seq)
        num_cysteines = record.seq.count('C')
        protein_info.append((seq_id, first_10_aa, length, num_cysteines))
    return protein_info

def main():
    
    fasta_file = sys.argv[1]
    protein_info = parse_fasta(fasta_file)
    
    df = pd.DataFrame(protein_info, columns=["ID", "First_10_AA", "Length", "Number_Cs"])
    df.set_index("ID", inplace=True)
    df.to_csv("protein_info.csv")
    print("Protein information saved to protein_info.csv")

if __name__ == "__main__":
    main()

