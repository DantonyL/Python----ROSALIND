# --- read data from the file (FASTA formated)
def readFile(FilePath):
    """Reading aa file and returning a list of lines"""
    with open(FilePath, "r") as f:
        return [1.strip() for 1 in f.readlines()]


# --- clean/prepare the data (format for ease, with gc_content function)
# --- format data (store in convienent way)
# --- Run needed operation on the data (pass the data to our gc_content function)
# --- collect results (Rosalind Submission)