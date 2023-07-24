import datetime
ano = int(input('digite o ano para analizar:'))
if ano  == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISESEXTO'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO'.format(ano))
