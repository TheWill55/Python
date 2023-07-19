vel = float(input('velocidade atual do carro!'))
if vel > 80:
    print('Você foi multado por exeder o limite de velocidade de 80km/h!')
    mult = 7 * (vel - 80)
    print('Você deve pagar no total de R$ {} em multa por exesso de velocidade!'.format(mult))
print('Velocidade atual segura, use cinto de segurança, tenha um bom dia!')