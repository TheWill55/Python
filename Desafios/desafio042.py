seg1 = int(input('Primeiro seguimento: '))
seg2 = int(input('Segundfo seguimento: '))
seg3 = int(input('Terceiro seguimento: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Tiangulo pode ser formado')
    if seg1 == seg2 == seg3:
        print('O Triangulo é EQUILÁTERO!')
    elif seg1 != seg2 != seg3 != seg1:
        print('O Triangulo é ESCALENO!')
    else:
        print('O Triangulo é ISÓSCELES!')
else:
    print('Não é possivel fazer o triangulo')