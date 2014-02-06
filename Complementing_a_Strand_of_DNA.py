f = open('rosalind_revc.txt', 'r')
line = f.read()
sf = ''
idx = line.count('') - 2
while idx >= 0:
    if line[idx] == 'A':
        sf = sf + 'T'
    if line[idx] == 'C':
        sf = sf + 'G'
    if line[idx] == 'G':
        sf = sf + 'C'
    if line[idx] == 'T':
        sf = sf + 'A'
    idx = idx - 1

f.close()