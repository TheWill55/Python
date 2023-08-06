fra = str(input('Digite uma frase: ')).strip().upper()
palavras = fra.split()
jun = ''.join(palavras)
invers = ''
for letra in range(len(jun), -1, -1, -1):
    invers = invers + jun[letra]
if invers == jun:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo!')