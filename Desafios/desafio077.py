estudos = ('python', 'javascript', 'php', 'java', 'portugol', 'react', 'kivy', 'games', 'minecraft', 'fortnite', 'warzone', 'godofwar')

for palavra in estudos:
	print(f'\nNa palavra {palavra.upper()} temos - ', end='')
	for letra in palavra:
		if letra.lower() in 'aeiou':
			print(letra, end=' ')