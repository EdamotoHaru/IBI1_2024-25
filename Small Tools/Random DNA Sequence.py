length = int(input("Enter the length of the DNA sequence: "))
# Generate a random DNA sequence of the specified length
import random
def generate_random_dna(length):
    # Define the possible nucleotides
    nucleotides = ['A', 'C', 'G', 'T']
    # Generate a random sequence of the specified length
    return ''.join(random.choice(nucleotides) for _ in range(length))
# Generate the random DNA sequence
random_dna_sequence = generate_random_dna(length)
# Print the generated sequence
print("Random DNA sequence of length", length, ":", random_dna_sequence)