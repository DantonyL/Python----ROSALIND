DNAStr = "GACGCCCTATATATAAGTCACTAGCGCGCATAATTCGGGCAGGGACAATTATGCTGTCGGCGGGCCATGTTATCGCCACGAGCAATTACCGTATGATTTATGACTGTCCCGATGATTGTAACAGAAGTTCGTGTGAAACCGCACGCCGGCCGTGAGTGCCTTACCAAATGCGCTAGACAGTAGCGACACAATGCTACTGCCTAGGTTGTCGAACGAGGCCACAAGGTATAGACAGTTCGGACAATCAATGCGTCATAGCCTCGAGATGTTTTCGTAGACGAACCATTCAACTCAGACGGATTACATGTCTCACGCTTGTTTAGCCCAATGTCCTAAGTATCCGAGCACCGTGTACAGTCCTCGACACCGGAAGGTTCACTTGCCTGCAGGGTAGCACGAGCCTTCATCCGGTCGCTTGTTATTTTCGAAAGACCAGTACCGCTATGTATAACGAGTCCGCTGTTACCACCGCTTAAATGCGAGTTTCAAAGTGAGACTGGTGAGACGGAACGACCGCGGCGTTTTTAACCGTCGTTAACGACAACTGTTAACCGAGATCTTCAGACCACGCATGCGATATGGGGAGACTGCTTGTAATGGGTCATCTATTGGTACGCATTCCACTACTCAGTACCATTGTGGGGTATCATTTGCTACCAATTAGTAAGTTGGACGATGTTGCGGCCCGCTGAAACTTCTTCGCGCCTGGTGCTGCCTGATGCGGTGATCTACGAGTGGGCATTTAACCCACATTGGCATAAGACTGCCCCGCCATACGCTTCGCGATCGGTCTCCAACCATTCTCAGGCAACTTCGAGGGTGGAGCTTACTAGACGAATGCTCTTCCGGAATTTCACGAGCAATCTGTATCATATTAAGGCCGCTTCAAGGTGACTGCACGCAGCGTCCTAAGAGGGCACTTATGATGTCTACCACATAGCTGATCCAGCACCCCCTGGTTATCAAAAGCTTTCTCATGCGTGCT"

def transcription(seq):
    """DNA -> RNA Transcription. Replacing Thymine(T) with Uracil(U)"""
    return seq.replace("T", "U")
print(transcription(DNAStr))