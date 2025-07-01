"""This is a simple DNA Analyzer that takes fasta files as input and outputs certain information about the contents of
the file"""

# import biopython

def main():
    """ Main function """

    def analyze_dna(sequence):
        """This function takes a DNA string as input and outputs certain information"""
        if isinstance(sequence, str):
            dna_seq = sequence.upper()
        else:
            print("The DNA sequence is not a string.")
            return None
        dna_length = len(dna_seq) # Finds length of DNA sequence after verifying the sequence itself.

        nuc_dict = {"A":0, "C":0, "G":0, "T":0}
        for base in dna_seq:
            base.upper()
            if base in nuc_dict:
                nuc_dict[base] += 1

        gc_percent = (nuc_dict["G"] + nuc_dict["C"]) / dna_length


        print(f"The GC percentage is {gc_percent}, and the counts for each base are {nuc_dict}.")
        return gc_percent, dna_length



    test_sequence = "AGCTTCGA"
    print("Analyzing sequence:", test_sequence)
    analyze_dna(test_sequence)

if __name__ == "__main__":
    main()
