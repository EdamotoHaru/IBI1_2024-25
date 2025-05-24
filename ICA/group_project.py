#example SARS-CoV-2 Spike RBD mRNA Sequence: 
#AUGGUGUUGAGAAGUUCAACGCUGAACGCAGACGACGACGGCCAGGACCAGGUGCUGGUACCCGCGAAGAAGCUGGCUCUGAGCGGCCUGGCGGUGCUGAUUGCUGGCACCGGCUCAGGCCAAGGAGUUGCUGUAGGCUGGAGGCAGUUGAGUUCUGUGGCUGGACACCUACUCCCGGACGAGGCUGCUGCUGAGGACCUGGAGGUGAUCAAGCCACAGUAGGCGAACUCGUGUAGAGUGUGAAGCGACCAGUCAGCCGGGCGAGUCUUGGGACAAAUCGAGUUGUACAGGUGCGUCAAUGGCUUCGAGGUGUACCGGCAGCGGAUCUUCAACGCAGAGUUAUGAGAACGGCUUCUUUCGUUGCACUGCGGCUUCGUCCGUGCGGCGUGCAACCAGGUGUCCCGUGCCCGACUACGUGCGAGCACGUCCGUGCGGCACCGUCAUCGGCGCUGUCGCUCGCUGGUCCCACCCCGUAGGUCACGCGCUGAAAAAAUUCUCCUGCCGCGCCAUCGCGAACGAGAAAGCGGACGAGGUCACAGGUUGUGUUAGCACGCUACACUACGUGCCGAGUCCUCGGCGGCU
import sys
import matplotlib.pyplot as plt

#condon table
codon_table={
'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'Stop', 'UAG': 'Stop',
'UGU': 'Cys', 'UGC': 'Cys', 'UGA': 'Stop', 'UGG': 'Trp',
'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met',
'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'
}

human_preferred_codon = {
    'UUU': 'UUC', 'UUC': 'UUC',  # Phe
    'UUA': 'CUG', 'UUG': 'CUG',  # Leu
    'CUU': 'CUG', 'CUC': 'CUG', 'CUA': 'CUG', 'CUG': 'CUG',
    'AUU': 'AUC', 'AUC': 'AUC', 'AUA': 'AUC',  # Ile
    'AUG': 'AUG',  # Met
    'GUU': 'GUG', 'GUC': 'GUG', 'GUA': 'GUG', 'GUG': 'GUG',  # Val
    'UCU': 'AGC', 'UCC': 'AGC', 'UCA': 'AGC', 'UCG': 'AGC', 'AGU': 'AGC', 'AGC': 'AGC',  # Ser
    'CCU': 'CCG', 'CCC': 'CCG', 'CCA': 'CCG', 'CCG': 'CCG',  # Pro
    'ACU': 'ACC', 'ACC': 'ACC', 'ACA': 'ACC', 'ACG': 'ACC',  # Thr
    'GCU': 'GCC', 'GCC': 'GCC', 'GCA': 'GCC', 'GCG': 'GCC',  # Ala
    'UAU': 'UAC', 'UAC': 'UAC',  # Tyr
    'UAA': 'UAA', 'UAG': 'UAA', 'UGA': 'UAA',  # Stop codons
    'CAU': 'CAC', 'CAC': 'CAC',  # His
    'CAA': 'CAG', 'CAG': 'CAG',  # Gln
    'AAU': 'AAC', 'AAC': 'AAC',  # Asn
    'AAA': 'AAG', 'AAG': 'AAG',  # Lys
    'GAU': 'GAC', 'GAC': 'GAC',  # Asp
    'GAA': 'GAG', 'GAG': 'GAG',  # Glu
    'UGU': 'UGC', 'UGC': 'UGC',  # Cys
    'UGG': 'UGG',  # Trp
    'CGU': 'CGG', 'CGC': 'CGG', 'CGA': 'CGG', 'CGG': 'CGG', 'AGA': 'CGG', 'AGG': 'CGG',  # Arg
    'GGU': 'GGC', 'GGC': 'GGC', 'GGA': 'GGC', 'GGG': 'GGC'   # Gly
}

#----------------------------Task 1-3 --------------------------------

#check the length and nucleotides of the sequence
def check_seq(seq):
    if len(seq)<10:
        sys.exit('Sequence too short')
    for nucleotide in seq:
        if nucleotide not in ['A','C','G','U']:
            sys.exit('sequence contains non-nucleotide characters')

#find the start codon
def find_start_codon(seq):
    coding_seq = ''
    for i in range(len(seq) - 2):
        if seq[i:i+3] == 'AUG':
            coding_seq = seq[i:]
            return coding_seq
    sys.exit('no start codon found! enter a valid sequence')

def count(coding_seq):
    codon_count = {}
    amino_acid_count = {}

    #count thenumber of each codon in the sequence
    for k in range(0, len(coding_seq), 3):
        if k + 3 <= len(coding_seq):
            codon = coding_seq[k:k+3]
            amino_acid = codon_table[codon]
            if amino_acid == 'Stop':
                break

            #count codons
            if codon in codon_count:
                codon_count[codon] += 1
            else:
                codon_count[codon] = 1
            
            #count amino acids
            if amino_acid in amino_acid_count:
                amino_acid_count[amino_acid] += 1
            else:
                amino_acid_count[amino_acid] = 1

    #find the most frequent codon and amino acid
    max_codon_count = max(codon_count.values())
    most_frequent_codon = [codon for codon, codon_count in codon_count.items() if codon_count == max_codon_count]

    max_aa_count = max(amino_acid_count.values())
    most_frequent_aa = [aa for aa, aa_count in amino_acid_count.items() if aa_count == max_aa_count]

    #print the most frequent nucleotide
    print('The most frequent codon is:', most_frequent_codon, 'Frequency:', max_codon_count)
    print('The most frequent amino acid is:', most_frequent_aa, 'Frequency:', max_aa_count)

    return amino_acid_count

#plot the frequency distribution of amino acids
def plot_fre(amino_acid_count):
    plt.bar(list(amino_acid_count.keys()), list(amino_acid_count.values()), label='Amino acid frequency')
    plt.xlabel('Amino Acid')
    plt.ylabel('Frequency')
    plt.title('Frequency distribution of encoded amino acids')
    plt.xticks(rotation=-45)
    plt.legend()
    plt.show()

#----------------------------Task 4 -----------------------------------------------

#Task4: mRNA vaccine design based on the Receptor Binding Domain of the antigen
#optimized mRNA into human preferred
def optimized_mRNA_seq(RBD_mrna):
    optimized_mRNA = ''
    for i in range(0,len(RBD_mrna),3):
        codon = RBD_mrna[i:i+3]
        optimized_codon = human_preferred_codon[codon]
        optimized_mRNA += optimized_codon
    return optimized_mRNA

#modified the mRNA seq, adding 5', 3' UTRs and polyA tail
def modified_mRNA_seq(optimized_mRNA):
    UTR5 = 'GCCACCAUGG' # Example 5' UTR with Kozak sequence
    UTR3 = 'AAUAAAUAUGAUCCUCUUUUAUCUAAGG'     # Example 3' UTR with N-terminal signal peptide
    PolyA = 'A' * 100     # PolyA tail
    mRNA_vaccine = UTR5 + optimized_mRNA + UTR3 + PolyA
    return mRNA_vaccine

#---------------------------- Main -----------------------------------------------

#find the most frequent nucleotide
def main():
    #example SARS-CoV-2 Spike RBD mRNA Sequence: 
    #AUGGUGUUGAGAAGUUCAACGCUGAACGCAGACGACGACGGCCAGGACCAGGUGCUGGUACCCGCGAAGAAGCUGGCUCUGAGCGGCCUGGCGGUGCUGAUUGCUGGCACCGGCUCAGGCCAAGGAGUUGCUGUAGGCUGGAGGCAGUUGAGUUCUGUGGCUGGACACCUACUCCCGGACGAGGCUGCUGCUGAGGACCUGGAGGUGAUCAAGCCACAGUAGGCGAACUCGUGUAGAGUGUGAAGCGACCAGUCAGCCGGGCGAGUCUUGGGACAAAUCGAGUUGUACAGGUGCGUCAAUGGCUUCGAGGUGUACCGGCAGCGGAUCUUCAACGCAGAGUUAUGAGAACGGCUUCUUUCGUUGCACUGCGGCUUCGUCCGUGCGGCGUGCAACCAGGUGUCCCGUGCCCGACUACGUGCGAGCACGUCCGUGCGGCACCGUCAUCGGCGCUGUCGCUCGCUGGUCCCACCCCGUAGGUCACGCGCUGAAAAAAUUCUCCUGCCGCGCCAUCGCGAACGAGAAAGCGGACGAGGUCACAGGUUGUGUUAGCACGCUACACUACGUGCCGAGUCCUCGGCGGCU
    seq = input('enter mRNA sequence:').upper().replace(' ','')
    check_seq(seq)
    coding_seq = find_start_codon(seq)
    amino_acid_count = count(coding_seq)

    #optimized mRNA sequence and modified mRNA vaccine sequence
    optimized_mRNA = optimized_mRNA_seq(seq)
    mRNA_vaccine = modified_mRNA_seq(optimized_mRNA)
    print('Optimized COVID-19 mRNA vaccine sequence:', mRNA_vaccine)

    #plot the frequency distribution of amino acids
    plot_fre(amino_acid_count)

if __name__ == '__main__':
    main()