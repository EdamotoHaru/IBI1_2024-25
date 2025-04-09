import random
length = int(input("Enter the length of the RNA sequence: "))
start_codon = random.choice(['AUG', 'AUA', 'AUC', 'AUG'])
stop_codon = random.choice(['UAA', 'UAG', 'UGA'])
def generate_random_rna(length):
    # Define the possible nucleotides
    nucleotides = ['A', 'C', 'G', 'U']
    # Generate a random sequence of the specified length
    return ''.join(random.choice(nucleotides) for _ in range(length))
# Generate the random RNA sequence
random_rna_sequence = generate_random_rna(length)
# Print the generated sequence
print("Random RNA sequence of length", length, ":", random_rna_sequence)
# Print the start and stop codons
print("Start codon:", start_codon)
print("Stop codon:", stop_codon)
# Find the start and stop codon positions
start_codon_position = random_rna_sequence.find(start_codon)
stop_codon_position = random_rna_sequence.find(stop_codon)
# Print the positions of the start and stop codons
print("Start codon position:", start_codon_position)
print("Stop codon position:", stop_codon_position)
