f = open('rosalind_revc.txt', 'r')
line = f.read()

k = 3
n = 5
x = k
y = k
i = 1
suma = 0
while i < n:
    suma = x + y
    y = x
    x = suma
    i = i + 1

suma

f.close()