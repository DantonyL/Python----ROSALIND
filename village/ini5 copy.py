f = open("village/data/rosalind_ini5.txt", "r")
output = open("village/data/out.txt", "w")
i = 1

for line in f.readlines():
	if i % 2 == 0:
		output.write(line)
	i = i + 1
print
