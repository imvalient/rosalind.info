f = open('insertion_sort_input.txt', 'r')

n = int(f.readline().strip())

lista = map(int, f.read().split())

print lista

def insertionSort(lista_):
    i = 0
    num = 0
    while i < n:
        k = i
        while k >= 1 and lista_[k] < lista_[k - 1]:
            aux = lista_[k]
            lista_[k] = lista_[k-1]
            lista_[k - 1] = aux
            num = num + 1
            k = k - 1
        i = i + 1
    return num

f = open('insertion_sort_result.txt', 'w')
f.write(str(insertionSort(lista)))
print lista