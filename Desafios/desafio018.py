import math
angu = float(input('Digite o ângulo que você deseja:'))
sen = math.sin(math.radians(angu))
print('O ângulo {:.0f} tem o SENO de {:.2f}'.format(angu,sen))
cos = math.cos(math.radians(angu))
print('O ângulo {:.0f} tem o COSENO de {:.2f}'.format(angu,cos))
tang = math.tan(math.radians(angu))
print('O ângulo {:.0f} tem o TANGENTE de {:.2f}'.format(angu,tang))

