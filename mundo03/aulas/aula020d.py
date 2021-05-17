def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [3, 6, 8, 10]
dobra(valores)
print(valores)