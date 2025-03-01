output_file = []
with open("village/data/rosalind_ini5.txt", "r") as f:
    output_file = [line for pos, line in enumerate(
        f.readlines()) if pos % 2 != 0]

with open("village/data/out.txt", "w") as f:
    f.write("".join([line for line in output_file]))
    
