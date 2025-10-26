"""
larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
area = larg * alt
print('Sua parede tem a dimensão de {} x {} e sua area total é de {}'.format(larg,alt,area))
tinta = area / 2
print('Para poder pintar sua parede você vai precisar de {}l de tinta'.format(tinta))
"""

print('======CALCULADORA DE BITCOIN======')
print('Bitcoin -- USD 30.333')
btc = float(input('Quantidade:'))
value = 30333
total1 = btc * value
print('Total de BTC:{} Convertido em dolar: USD{:.2f}'.format(btc,total1))
print('Total em BRL: R${:.2f}'.format(total1 * 4.92))


print('====== CALCULADORA DE BITCOIN ======')

bitcoin_to_usd = 30333  # Valor do Bitcoin em USD
btc = float(input('Quantidade de Bitcoin: '))

total_usd = btc * bitcoin_to_usd
total_brl = total_usd * 4.92

print(f'Total de BTC: {btc} Convertido em dólar: USD {total_usd:.2f}')
print(f'Total em BRL: R$ {total_brl:.2f}')
