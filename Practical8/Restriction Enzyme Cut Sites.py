DNA = str(input("Enter the DNA sequence: "))  # Prompt user for DNA sequence
enzyme = str(input("Enter the restriction enzyme recognition sequence: "))  # Prompt user for enzyme sequence
def find_cut_site(DNA, enzyme):
    valid = set('ACGT')
    if set(DNA) - valid or set(enzyme) - valid:
        print("Error: Sequences must contain only A, C, G, T")
        return None
    position = DNA.find(enzyme)
    if position == -1:
        print("Error: For restriction enzyme" , enzyme , "recognition sequence not found")
        return None
    return position

print("The cut site for this DNA is at the" , find_cut_site(DNA , enzyme), "position")