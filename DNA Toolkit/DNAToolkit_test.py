from DNA_Toolkit import *
from utilities import colored
import random

DNAStr = (validateSeq(randDNAStr))
print(f"\nSequence: {DNAStr}\n")

print(f"\nSequence: {colored(DNAStr)}\n")
print(f"[1] + Sequence Length: {len(DNAStr)}\n")
print(colored(f"[2] + Nucleotide Frequence: {countNucFrequency(DNAStr)}\n"))
print(f"[3] + DNA/RNA Transcription: {colored(transcription(DNAStr))}\n")
print(f"[4] + DNA String Reverse Compliment: \n5' {colored(DNAStr)} 3'")
print(f"   {"".join(['|' for c in range(len(DNAStr))])}")
print(f"3' {reverse_compliment(DNAStr)[::-1]} 5' [Compliment]")
print(f"5' {reverse_compliment(DNAStr)} 3' [Reverse Compliment]")