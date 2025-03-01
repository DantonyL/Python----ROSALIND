# DNA ToolKit

Nucleotides = ["A", "C", "G", "T"]

### Check the sequence to make sure it is a DNA String
# function = validateSeq()
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


### Creating a Random DNA sequence for testiing:
import random

randDNAStr = ''.join([random.choice(Nucleotides)
                      for nuc in range(50)])
print(validateSeq(randDNAStr))



### Count Nucleotide Frequency:
def countNucFrequency(seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T":0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict
print(countNucFrequency(randDNAStr))

# Count using python collections
import collections
def countNucFrequency2(seq):
    return dict(collections.Counter(seq))
print(countNucFrequency2(randDNAStr))

### Transcription DNA -> RNA 
def transcription(seq):
    """DNA -> RNA Transcription. Replacing Thymine(T) with Uracil(U)"""
    return seq.replace("T", "U")
print(transcription(randDNAStr))

# Reverse Compliment (1st positon becomes last // A <-> T(U) or G <-> C
DNA_ReverseCompliment = {"A": "T", "T": "A", "G": "C", "C": "G"}

def reverse_compliment(seq):
    """Swapping Adenine(A) with Thymine(T) and Guanine(G) with Cytosine(C). Reversing Newly Generated String"""
    return "".join([DNA_ReverseCompliment[nuc] for nuc in seq])[::-1]

    #pythonic apporach, faster solution (hard to translate)
    #mapping = str.maketrans("ATCG", "TAGC")
    #return seq.translate(mapping)[::-1]


### GC Content Calculation
def gc_content(seq):
    """GC Content in a DNA/RNA Sequence"""
    return round((seq.count("C") + seq.count("G")) / len(seq) * 100)