from Bio.Blast import NCBIWWW, NCBIXML

# define the query sequence
# Here, we are using a hypothetical protein sequence as an example.
query_sequence = "MLSRAVCGTSRQLAPVLGYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK"

# On the NCBI server, perform a BLAST search (After trying we find it takes a long time to get results)
result_handle = NCBIWWW.qblast("blastp", "nr", query_sequence)

# Store the results in an XML file
with open("blast_results.xml", "w") as out_handle:
    out_handle.write(result_handle.read())
result_handle.close()

# Read the results from the XML file
with open("blast_results.xml") as result_file:
    blast_records = NCBIXML.parse(result_file)

    # Iterate through the BLAST records and print the results
    for record in blast_records:
        for alignment in record.alignments:
            for hsp in alignment.hsps:
                if hsp.expect < 0.01:  # Choose a threshold for E-value 0.01
                    print(f"Sequence: {alignment.title}")
                    print(f"E Value: {hsp.expect}")
                    print(f"Similarity: {hsp.identities / hsp.align_length * 100:.2f}%")
                    print("---")