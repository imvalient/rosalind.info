f = open('rosalind_rna.txt', 'r')
line = f.read()
line.replace('T', 'U')
f.close()