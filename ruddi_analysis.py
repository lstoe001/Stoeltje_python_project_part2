#!/usr/bin/env python

import sys
import csv
from Bio import SeqIO

def calculate_metrics(genome_sequence):
    length_of_genome = len(genome_sequence)
    gc_content = ((genome_sequence.count("G") + genome_sequence.count("C")) / length_of_genome) * 100
    occurrences_forward = genome_sequence.count("ATG")
    occurrences_reverse = genome_sequence.reverse_complement().count("ATG")
    return length_of_genome, gc_content, occurrences_forward, occurrences_reverse

def main():
    
    fasta_file = sys.argv[1]

    # Parse the FASTA file
    records = SeqIO.parse(fasta_file, "fasta")
    for record in records:
        genome_sequence = record.seq
        break  # Only process the first record assuming there's only one genome sequence

    # Calculate metrics
    length_of_genome, gc_content, occurrences_forward, occurrences_reverse = calculate_metrics(genome_sequence)

    # Write metrics to CSV
    with open("ruddi.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Length_of_genome", "GC_content", "ATG_forward", "ATG_reverse"])
        writer.writerow([length_of_genome, gc_content, occurrences_forward, occurrences_reverse])


if __name__ == "__main__":
    main()

