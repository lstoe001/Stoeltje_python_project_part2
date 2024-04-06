import os
from Bio import SeqIO
import pandas as pd


def parse_genbank(genbank_file):
    records = []
    for record in SeqIO.parse(genbank_file, "genbank"):
        accession = record.id
        family = genus = species = source = 'unknown'  # Initialize variables
        
        if 'taxonomy' in record.annotations:
            taxonomy = record.annotations['taxonomy']
            if len(taxonomy) >= 2:
                family = taxonomy[-2]
                genus = taxonomy[-3]
                species = taxonomy[-1]
            elif len(taxonomy) == 1:
                genus = taxonomy[-1]
                
        num_features = len(record.features)
        source = record.annotations.get("source", "")
        records.append((accession, family, genus, species, num_features, source))
    return records

def main():
    # Gets the path to the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Searches for GenBank files in the current directory
    genbank_files = [file for file in os.listdir(current_dir) if file.endswith(".gbk")]

    # Processes each GenBank file
    all_records = []
    for genbank_file in genbank_files:
        genbank_path = os.path.join(current_dir, genbank_file)
        records = parse_genbank(genbank_path)
        all_records.extend(records)

    # Creates a DataFrame from all records
    df = pd.DataFrame(all_records, columns=["Accession", "Family", "Genus", "Species", "Num_Features", "Source"])
    # Save DataFrame to CSV file
    output_file = "genbank_parse.csv"
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    main()

