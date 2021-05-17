frase = str(input('Digite uma frase: ')).strip().upper()
div = frase.split()
junto = ''.join(div)
inverso = ''
for letra in range (len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(inverso, junto, 'Sua palavra é um palíndromo!')
else:
    print('Sua frase não é uma palíndromo!')