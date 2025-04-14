import random
from collections import Counter
import matplotlib.pyplot as plt

# Codon to amino acid mapping (excluding stop codons)
codon_to_aa = {
    "UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
    "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
    "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met",
    "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
    "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
    "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "UAU": "Tyr", "UAC": "Tyr",
    "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
    "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
    "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
    "UGU": "Cys", "UGC": "Cys", "UGG": "Trp",
    "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
    "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
    "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"
}

def get_codons(seq):
    """
    Extract codons from the mRNA sequence until a stop codon is encountered.
    Parameters:
        seq (str): mRNA sequence, assumed to start with 'AUG'.
    Returns:
        list: List of codons, excluding the stop codon.
    """
    stop_codons = ["UAA", "UAG", "UGA"]
    codons = []
    for i in range(0, len(seq), 3):
        if i + 3 > len(seq):
            break
        codon = seq[i:i+3]
        if codon in stop_codons:
            break
        codons.append(codon)
    return codons

def most_frequent_codons(seq):
    """
    Find the most frequent codons in the sequence.
    Parameters:
        seq (str): mRNA sequence.
    Returns:
        tuple: (list of most frequent codons, frequency).
    """
    codons = get_codons(seq)
    if not codons:
        return [], 0
    count = Counter(codons)
    max_freq = max(count.values())
    most_frequent = [codon for codon, freq in count.items() if freq == max_freq]
    return most_frequent, max_freq

def most_frequent_aas(seq):
    """
    Compute the amino acids corresponding to the most frequent codons.
    Parameters:
        seq (str): mRNA sequence.
    Returns:
        list: List of unique amino acids.
    """
    most_freq_codons, _ = most_frequent_codons(seq)
    aas = [codon_to_aa.get(codon, "Unknown") for codon in most_freq_codons]
    return list(set(aas))

def plot_aa_frequencies(seq):
    """
    Plot the frequency distribution of amino acids in the sequence.
    Parameters:
        seq (str): mRNA sequence.
    """
    codons = get_codons(seq)
    aas = [codon_to_aa.get(codon, "Unknown") for codon in codons]
    if not aas:
        print("No amino acids to plot.")
        return
    count = Counter(aas)
    amino_acids = list(count.keys())
    frequencies = list(count.values())
    # Sort by amino acid name
    sorted_indices = sorted(range(len(amino_acids)), key=lambda x: amino_acids[x])
    sorted_aas = [amino_acids[i] for i in sorted_indices]
    sorted_freq = [frequencies[i] for i in sorted_indices]
    plt.figure(figsize=(10, 6))
    plt.bar(sorted_aas, sorted_freq, color='skyblue')
    plt.xlabel('Amino Acid')
    plt.ylabel('Frequency')
    plt.title('Amino Acid Frequency Distribution')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_codon_frequencies(seq):
    """
    Plot the frequency distribution of codons in the sequence (additional feature).
    Parameters:
        seq (str): mRNA sequence.
    """
    codons = get_codons(seq)
    if not codons:
        print("No codons to plot.")
        return
    count = Counter(codons)
    codons_list = list(count.keys())
    frequencies = list(count.values())
    # Sort by codon name
    sorted_indices = sorted(range(len(codons_list)), key=lambda x: codons_list[x])
    sorted_codons = [codons_list[i] for i in sorted_indices]
    sorted_freq = [frequencies[i] for i in sorted_indices]
    plt.figure(figsize=(12, 6))
    plt.bar(sorted_codons, sorted_freq, color='lightgreen')
    plt.xlabel('Codon')
    plt.ylabel('Frequency')
    plt.title('Codon Frequency Distribution')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Get user input for mRNA sequence
    seq = input("Enter the mRNA sequence: ").upper().replace(" ", "")
    print("Input sequence:", seq)
    
    # Task 1: Most frequent codons
    most_freq_codons, freq = most_frequent_codons(seq)
    if most_freq_codons:
        print(f"Most frequent codons: {', '.join(most_freq_codons)}, frequency: {freq}")
        
        # Task 2: Corresponding amino acids
        most_freq_aas = most_frequent_aas(seq)
        print(f"Corresponding amino acids: {', '.join(most_freq_aas)}")
        
        # Task 3: Plot amino acid frequencies
        plot_aa_frequencies(seq)
        
        # Task 4: Plot codon frequencies
        plot_codon_frequencies(seq)
    else:
        print("No codons found in the sequence.")